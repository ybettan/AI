from framework.graph_search import *
from framework.ways import *

from typing import Iterator, Tuple


class MapState(GraphProblemState):
    """
    Map state is represents the current geographic location on the map.
    This location is defined by the junction index.
    """

    def __init__(self, junction_id: int):
        self.junction_id = junction_id

    def __eq__(self, other):
        assert isinstance(other, MapState)
        return other.junction_id == self.junction_id

    def __hash__(self):
        return hash(self.junction_id)

    def __str__(self):
        return str(self.junction_id).rjust(5, ' ')


class MapProblem(GraphProblem):
    """
    Represents a problem on the geographic map.
    The problem is defined by a source location on the map and a destination.
    """

    name = 'Map'

    def __init__(self, roads: Roads, source_junction_id: int, target_junction_id: int):
        initial_state = MapState(source_junction_id)
        super(MapProblem, self).__init__(initial_state)
        self.roads = roads
        self.target_junction_id = target_junction_id
        self.name += '(src: {} dst: {})'.format(source_junction_id, target_junction_id)
    
    def expand_state_with_costs(self, state_to_expand: GraphProblemState) -> Iterator[Tuple[GraphProblemState, float]]:
        """
        For a given state, iterates over its successor states.
        The successor states represents the junctions to which there
        exists a road originates from the given state.
        """

        # All of the states in this problem are instances of the class `MapState`.
        assert isinstance(state_to_expand, MapState)

        # Get the junction (in the map) that is represented by the state to expand.
        junction = self.roads[state_to_expand.junction_id]

        # Iterate over the outgoing roads of the current junction.
        for link in junction.links:
            # Create the successor state (it should be an instance of class `MapState`).
            successor_state = MapState(link.target)

            # TODO: calculate the distance between `junction` and the successor's junction.
            # Use the method `calc_air_distance_from()` of class `Junction` to measure this distance.
            # Do NOT use `link.distance` here.
            operator_cost = 1  # TODO: modify this!

            # Yield the successor state and the cost of the operator we used to get this successor.
            yield successor_state, operator_cost

    def is_goal(self, state: GraphProblemState) -> bool:
        """
        :return: Whether a given map state represents the destination.
        """
        assert (isinstance(state, MapState))

        # TODO: modify the returned value to indicate whether `state` is a final state.
        # You may use the problem's input parameters (stored as fields of this object by the constructor).
        return state.junction_id == 14593
