import abc
from typing import Iterator, Tuple, Optional, Type, NamedTuple, Union, Callable


"""
We define `__all__` variable in order to set which names will be
imported when writing (from another file):
>>> from framework.graph_search.graph_problem_interface import *
"""
__all__ = ['GraphProblemState', 'GraphProblem', 'GraphProblemStatesPath', 'SearchNode',
           'SearchResult', 'GraphProblemSolver',
           'HeuristicFunction', 'HeuristicFunctionType', 'NullHeuristic']


class GraphProblemState(abc.ABC):
    """
    This class defines an *interface* used to represent a state of a states-space, as learnt in class.
    Notice that this is an *abstract* class. It does not represent a concrete state.
    The inheritor class must implement the abstract methods defined by this class.
    """

    @abc.abstractmethod
    def __eq__(self, other):
        """
        This is an abstract method that must be implemented by the inheritor class.
        This method is used to determine whether two given state objects represents the same state.
        Notice: Never compare floats using `==` operator!
        """
        ...

    @abc.abstractmethod
    def __hash__(self):
        """
        This is an abstract method that must be implemented by the inheritor class.
        This method is used to create a hash of a state.
        It is critical that two objects representing the same state would have the same hash!
        A common implementation might be something in the format of:
        >>> hash((self.some_field1, self.some_field2, self.some_field3))
        Notice: Do NOT give float fields to `hash()`. Otherwise the upper requirement would not met.
        """
        ...

    @abc.abstractmethod
    def __str__(self):
        """
        This is an abstract method that must be implemented by the inheritor class.
        This method is used by the printing mechanism of `SearchResult`.
        """


class GraphProblem(abc.ABC):
    """
    This class defines an *interface* used to represent a states-space, as learnt in class.
    Notice that this is an *abstract* class. It does not represent a concrete states-space.
    The inheritor class must implement the abstract methods defined by this class.
    By defining these abstract methods, the inheritor class represents a well-defined states-space.
    """

    """Each problem might have a name as a string. This name is used in the solution printings."""
    name: str = ''

    def __init__(self, initial_state: GraphProblemState):
        self.initial_state = initial_state

    @abc.abstractmethod
    def expand_state_with_costs(self, state_to_expand: GraphProblemState) -> Iterator[Tuple[GraphProblemState, float]]:
        """
        This is an abstract method that must be implemented by the inheritor class.
        This method represents the `Succ: S -> P(S)` function learnt in class.
        It receives a state and iterates over the successor states.
        Notice that this is an *Iterator*. Hence it should be implemented using the `yield` keyword.
        For each successor, a pair of the successor state and the operator cost is yielded.
        """
        ...

    @abc.abstractmethod
    def is_goal(self, state: GraphProblemState) -> bool:
        """
        This is an abstract method that must be implemented by the inheritor class.
        It receives a state and returns whether this state is a goal.
        """
        ...

    def solution_additional_str(self, result: 'SearchResult') -> str:
        """
        This method may be overridden by the inheritor class.
        It is used to enhance the printing method of a found solution.
        We implemented it wherever needed - you do not have to care about it.
        """
        return ''


class GraphProblemStatesPath(Tuple[GraphProblemState]):
    """
    This class represents a path of states.
    It is just a tuple of GraphProblemState objects.
    We define a dedicated class in order to implement the string formatting method.
    """

    def __eq__(self, other):
        assert isinstance(other, GraphProblemStatesPath)
        if len(other) != len(self):
            return False
        return all(s1 == s2 for s1, s2 in zip(self, other))

    def __str__(self):
        return '[' + (', '.join(str(state) for state in self)) + ']'


class SearchNode:
    """
    An object of type `SearchNode` represent a node created by a search algorithm.
    A node basically has a state that it represents, and potentially a parent node.
    A node may also have its cost, the cost of the operator performed to reach this node,
    and the f-score of this node (expanding_priority) when needed.
    """

    def __init__(self, state: GraphProblemState,
                 parent_search_node: Optional['SearchNode'] = None,
                 operator_cost: float = 0,
                 expanding_priority: Optional[float] = None):
        self.state: GraphProblemState = state
        self.parent_search_node: SearchNode = parent_search_node
        self.operator_cost: float = operator_cost
        self.cost: Optional[float] = None
        self.expanding_priority: Optional[float] = expanding_priority

        self.cost = operator_cost
        if self.parent_search_node is not None:
            self.cost += self.parent_search_node.cost

    def traverse_back_to_root(self) -> Iterator['SearchNode']:
        """
        This is an iterator. It iterates over the nodes in the path
        starting from this node and ending in the root node.
        """
        node = self
        while node is not None:
            assert(isinstance(node, SearchNode))
            yield node
            node = node.parent_search_node

    def make_states_path(self) -> GraphProblemStatesPath:
        """
        :return: A path of *states* represented by the nodes
        in the path from the root to this node.
        """
        path = [node.state for node in self.traverse_back_to_root()]
        path.reverse()
        return GraphProblemStatesPath(path)


class SearchResult(NamedTuple):
    """
    It is the type of the object that is returned by `solver.solve_problem()`.
    It stores the results of the search.
    """

    """The solver that generated this result."""
    solver: 'GraphProblemSolver'
    """The problem that the solver has attempted to solve."""
    problem: GraphProblem
    """The node that represents the goal found. Set to `None` if no result had been found."""
    final_search_node: Optional[SearchNode]
    """The number of expanded states during the search."""
    nr_expanded_states: int
    """The time (in seconds) took to solve."""
    solving_time: float

    def __str__(self):
        """
        Enhanced string formatting for the search result.
        """

        res_str = '{problem_name: <35}' \
                   '   {solver_name: <27}' \
                   '   time: {solving_time:6.2f}' \
                   '   #dev: {nr_expanded_states: <5}'.format(
            problem_name=self.problem.name,
            solver_name=self.solver.solver_name,
            solving_time=self.solving_time,
            nr_expanded_states=self.nr_expanded_states
        )

        # no solution found by solver
        if self.final_search_node is None:
            return res_str + '   NO SOLUTION FOUND !!!'

        path = self.make_path()
        res_str += '   total_cost: {cost:11.5f}' \
                   '   |path|: {path_len: <3}' \
                   '   path: {path}'.format(
            cost=self.final_search_node.cost,
            path_len=len(path),
            path=str(path)
        )

        additional_str = self.problem.solution_additional_str(self)
        if additional_str:
            res_str += '   ' + additional_str

        return res_str

    def make_path(self):
        return self.final_search_node.make_states_path()


class GraphProblemSolver(abc.ABC):
    """
    This class is simply just an interface for graph search algorithms.
    Each search algorithm that we are going to implement will inherit
    from this class and implement the `solve_problem()` method.
    """

    """The solver name is used when printing the search results.
    It may be overridden by the inheritor algorithm."""
    solver_name: str = 'GraphProblemSolver'

    @abc.abstractmethod
    def solve_problem(self, problem: GraphProblem) -> SearchResult:
        ...


class HeuristicFunction(abc.ABC):
    """
    This is an interface for a heuristic function.
    Each implementation of a concrete heuristic function inherits from this class.
    """

    """Used by the solution printings.
    Might be overridden by the inheritor heuristic."""
    heuristic_name = ''

    def __init__(self, problem: GraphProblem):
        self.problem = problem

    @abc.abstractmethod
    def estimate(self, state: GraphProblemState) -> float:
        """
        Calculates and returns the heuristic value for a given state.
        This is an abstract method that must be implemented by the inheritor.
        """
        ...


"""Search algorithm which uses a heuristic may receive in their
constructor the type of the heuristic to use, rather than an
already-created instance of the heuristic."""
HeuristicFunctionType = Union[Type[HeuristicFunction], Callable[[GraphProblem], HeuristicFunction]]


class NullHeuristic(HeuristicFunction):
    """
    This is a simple implementation of the null heuristic.
    It might be used with A* for a sanity-check (A* should
    behave exactly like UniformCost in that case).
    """

    heuristic_name = '0'

    def estimate(self, state: GraphProblemState) -> float:
        return 0

