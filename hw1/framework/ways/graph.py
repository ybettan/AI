"""
 A set of utilities for using israel.csv 
 The map is extracted from the openstreetmap project
"""

from . import tools
import sys
from typing import List, Tuple, Dict, Iterator, Set, NamedTuple


# Some additional parameters for a link
class LinkTrafficParams(NamedTuple):
    cos_frequency: float
    sin_frequency: float


class Link(NamedTuple):
    source: int
    target: int
    distance: int
    highway_type: int
    link_params: LinkTrafficParams


class Junction(NamedTuple):
    index: int
    lat: float
    lon: float
    links: List[Link]

    @property
    def coordinates(self) -> Tuple[float, float]:
        return self.lat, self.lon

    def __eq__(self, other):
        if not isinstance(other, Junction):
            return False
        return self.index == other.index

    def __hash__(self):
        return hash(self.index)

    def calc_air_distance_from(self, other_junction: 'Junction') -> float:
        assert(isinstance(other_junction, Junction))
        return tools.compute_distance(self.coordinates, other_junction.coordinates)


class Roads(Dict[int, Junction]):
    """
    The graph is a dictionary Junction_id->Junction, with some methods to help.
    To change the generation, simply assign to it:
    g.generation = 5
    """

    def junctions(self) -> List[Junction]:
        return list(self.values())

    def __init__(self, junction_list: Dict[int, Junction]):
        super(Roads, self).__init__(junction_list)
        """to change the generation, simply assign to it"""
        self.generation = 0
        self.base_traffic = tools.base_traffic_pattern()
        tmp = [(n.lat, n.lon) for n in junction_list.values()]
        self.mean_lat_lon = (sum([i[0] for i in tmp]) / len(tmp), sum([i[1] for i in tmp]) / len(tmp))

    def return_focus(self, start_junction_id: int) -> Set[Link]:
        found = set()
        start_node = self[start_junction_id]
        _next = {l for l in start_node.links}
        while len(_next) > 0:
            _next_next = {l for k in _next for l in self[k.target].links if
                          l not in found}  # might even be able to drop the "l not in found" thing.
            found |= _next
            _next = _next_next
            if len(found) > 15:
                break
        return found

    def iterlinks(self) -> Iterator[Link]:
        """chain all the links in the graph.
        use: for link in roads.iterlinks(): ... """
        return (link for j in self.values() for link in j.links)


def _make_link(source_idx: int, link_string: str) -> Link:
    """This function is for local use only"""
    link_params = [int(x) for x in link_string.split("@")]
    assert len(link_params) == 3
    target_idx = link_params[0]
    distance = link_params[1]
    highway_type = link_params[2]
    link_traffic_params = LinkTrafficParams(*tools.generate_traffic_noise_params(source_idx, target_idx))
    return Link(source_idx, target_idx, distance, highway_type, link_traffic_params)


def _make_junction(idx_str: str, lat_str: str, lon_str: str, *link_row: str) -> Junction:
    """This function is for local use only"""
    idx, lat, lon = int(idx_str), float(lat_str), float(lon_str)
    try:
        links = [_make_link(idx, lnk) for lnk in link_row]
        links = list(filter(lambda lnk: lnk.distance > 0, links))
    except ValueError:
        links = []
    return Junction(idx, lat, lon, links)


@tools.timed
def load_map_from_csv(filename: str, start=0, count=sys.maxsize) -> Roads:
    """
    returns graph, encoded as an adjacency list
    @param slice_params can be used to cut part of the file
    example: load_map_from_csv(start=50000, count=50000))
    """

    import csv
    from itertools import islice
    with open(filename, 'rt') as f:
        it = islice(f, start, min(start + count, sys.maxsize))
        lst = {int(row[0]): _make_junction(*row) for row in csv.reader(it)}
        if count < sys.maxsize:
            lst = {i: Junction(i, j.lat, j.lon, [lnk for lnk in j.links if lnk.target in lst])
                   for i, j in lst.items()}
    return Roads(lst)
