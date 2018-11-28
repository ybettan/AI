from framework.graph_search import *
from framework.ways import *
from .map_problem import MapProblem
from .deliveries_problem_input import DeliveriesProblemInput
from .relaxed_deliveries_problem import RelaxedDeliveriesState, RelaxedDeliveriesProblem

from typing import Set, FrozenSet, Optional, Iterator, Tuple, Union


class StrictDeliveriesState(RelaxedDeliveriesState):
    """
    An instance of this class represents a state of the strict
     deliveries problem.
    This state is basically similar to the state of the relaxed
     problem. Hence, this class inherits from `RelaxedDeliveriesState`.
    """
    pass


class StrictDeliveriesProblem(RelaxedDeliveriesProblem):
    """
    An instance of this class represents a strict deliveries problem.
    """

    name = 'StrictDeliveries'

    def __init__(self, problem_input: DeliveriesProblemInput, roads: Roads,
                 inner_problem_solver: GraphProblemSolver, use_cache: bool = True):
        super(StrictDeliveriesProblem, self).__init__(problem_input)
        self.initial_state = StrictDeliveriesState(
            problem_input.start_point, frozenset(), problem_input.gas_tank_init_fuel)
        self.inner_problem_solver = inner_problem_solver
        self.roads = roads
        self.use_cache = use_cache
        self._init_cache()
        self.start_point = problem_input.start_point
        self.drop_points = frozenset(problem_input.drop_points)
        self.gas_stations = frozenset(problem_input.gas_stations)
        self.gas_tank_capacity = problem_input.gas_tank_capacity
        self.possible_stop_points = self.drop_points | self.gas_stations

    def _init_cache(self):
        self._cache = {}
        self.nr_cache_hits = 0
        self.nr_cache_misses = 0

    def _insert_to_cache(self, key, val):
        if self.use_cache:
            self._cache[key] = val

    def _get_from_cache(self, key):
        if not self.use_cache:
            return None
        if key in self._cache:
            self.nr_cache_hits += 1
        else:
            self.nr_cache_misses += 1
        return self._cache.get(key)

    def expand_state_with_costs(self, state_to_expand: GraphProblemState) -> Iterator[Tuple[GraphProblemState, float]]:
        """
        TODO: implement this method!
        This method represents the `Succ: S -> P(S)` function of the strict deliveries problem.
        The `Succ` function is defined by the problem operators as shown in class.
        The relaxed problem operators are defined in the assignment instructions.
        It receives a state and iterates over the successor states.
        Notice that this is an *Iterator*. Hence it should be implemented using the `yield` keyword.
        For each successor, a pair of the successor state and the operator cost is yielded.
        """
        assert isinstance(state_to_expand, StrictDeliveriesState)

        # Iterate over the unvisited drop points, dp : Junction
        for dp in self.drop_points:
            src_p = state_to_expand.current_location.index
            operator_cost = self._get_from_cache((src_p, dp.index))
            if not operator_cost:
                map_prob = MapProblem(self.roads, src_p, dp.index)
                operator_cost = self.inner_problem_solver.solve_problem(map_prob).final_search_node.cost
                self._insert_to_cache((src_p, dp.index), operator_cost)
            was_dropped_already = dp in state_to_expand.dropped_so_far
            # create only new and reachable successors
            if was_dropped_already or operator_cost > state_to_expand.fuel:
                continue
            new_dropped_so_far = set(state_to_expand.dropped_so_far)
            new_dropped_so_far.add(dp)
            new_fuel = state_to_expand.fuel - operator_cost
            successor_state = StrictDeliveriesState(dp, frozenset(new_dropped_so_far), new_fuel)

            # Yield the successor state and the cost of the operator we used to get this successor.
            yield successor_state, operator_cost

        # Iterate over the gas stations
        for gs in self.gas_stations:
            src_p = state_to_expand.current_location.index
            operator_cost = self._get_from_cache((src_p, gs.index))
            if not operator_cost:
                map_prob = MapProblem(self.roads, src_p, gs.index)
                operator_cost = self.inner_problem_solver.solve_problem(map_prob).final_search_node.cost
                self._insert_to_cache((src_p, gs.index), operator_cost)
            # create only reachable successors
            if operator_cost > state_to_expand.fuel:
                continue
            new_dropped_so_far = frozenset(state_to_expand.dropped_so_far)
            new_fuel = self.gas_tank_capacity
            successor_state = StrictDeliveriesState(gs, new_dropped_so_far, new_fuel)

            # Yield the successor state and the cost of the operator we used to get this successor.
            yield successor_state, operator_cost  # FIXME: cost instead of operator cost

    def is_goal(self, state: GraphProblemState) -> bool:
        """
        This method receives a state and returns whether this state is a goal.
        TODO: implement this method!
        """
        assert isinstance(state, StrictDeliveriesState)
        return state.dropped_so_far == self.drop_points
