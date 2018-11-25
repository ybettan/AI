from .graph_problem_interface import *
from .best_first_search import BestFirstSearch
from typing import Optional
import numpy as np


class GreedyStochastic(BestFirstSearch):
    def __init__(self, heuristic_function_type: HeuristicFunctionType,
                 T_init: float = 1.0, N: int = 5, T_scale_factor: float = 0.95):
        # GreedyStochastic is a graph search algorithm. Hence, we use close set.
        super(GreedyStochastic, self).__init__(use_close=True)
        self.heuristic_function_type = heuristic_function_type
        self.T = T_init
        self.N = N
        self.T_scale_factor = T_scale_factor
        self.solver_name = 'GreedyStochastic (h={heuristic_name})'.format(
            heuristic_name=heuristic_function_type.heuristic_name)

    def _init_solver(self, problem: GraphProblem):
        super(GreedyStochastic, self)._init_solver(problem)
        self.heuristic_function = self.heuristic_function_type(problem)

    def _open_successor_node(self, problem: GraphProblem, successor_node: SearchNode):
        """
        TODO: implement this method!
        """

        #raise NotImplemented()  # TODO: remove!

        is_in_open = self.open.has_state(successor_node.state)
        is_in_close = (self.close.get_node_by_state(successor_node.state)) != None

        if not is_in_open and not is_in_close:
            self.open.push_node(successor_node)

    def _calc_node_expanding_priority(self, search_node: SearchNode) -> float:
        """
        TODO: implement this method!
        Remember: `GreedyStochastic` is greedy.
        """

        #raise NotImplemented()  # TODO: remove!
        return self.heuristic_function.estimate(search_node.state)

    def pr(self, h, h_array, a):
        """
        given one of the heuristic values the method returns the probability
        of choosing this heuristic value over the other.
        """
        n_smallest = h_array[:self.N]
        return ((h/a)**(-1/self.T)) / sum([(s/a)**(-1/self.T) for s in n_smallest])

    def _extract_next_search_node_to_expand(self) -> Optional[SearchNode]:
        """
        Extracts the next node to expand from the open queue,
         using the stochastic method to choose out of the N
         best items from open.
        TODO: implement this method!
        Use `np.random.choice(...)` whenever you need to randomly choose
         an item from an array of items given a probabilities array `p`.
        You can read the documentation of `np.random.choice(...)` and
         see usage examples by searching it in Google.
        Notice: You might want to pop min(N, len(open) items from the
                `open` priority queue, and then choose an item out
                of these popped items. The other items have to be
                pushed again into that queue.
        """

        #raise NotImplemented()  # TODO: remove!
        picking_size = min(self.N, len(self.open))

        # get the picking_size nodes with the smallest h value
        first_poped = []
        for _ in range(picking_size):
            first_poped.append(self.open.pop_next_node())
        first_poped = np.array(first_poped)

        # create an array of h values
        h_array = np.array([self._calc_node_expanding_priority(node) for node in first_poped])
        a = min(h_array)

        # if a == 0 then we will chose the node with h = 0
        if a == 0:
            # find a node with h == 0
            res = [fp for fp in first_poped if self._calc_node_expanding_priority(fp) == 0][0]
        
        # else we choose randomaly
        else:
            # create the propabibily list
            probabilities = [self.pr(h, h_array, a) for h in h_array]

            # choose the next node to be developed
            res = np.random.choice(first_poped, p=probabilities)

        # put back all other nodes in OPEN
        for fp in first_poped:
            if fp != res:
                self.open.push_node(fp)

        # update Temperature for next interation
        self.T *= 0.95

        return res
         


