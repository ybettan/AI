ways/
Library for handling road map.

Most of the work is done with one function, `load_map_from_csv`, and three classes: `Junction`, `Link` and `Roads`.

##Functions

load_map_from_csv (start=0, count=sys.maxint
The workhorse of the library.

The basic usage is simple:
```python
from ways import load_map_from_csv
roads = load_map_from_csv()
# work with road
```
This function takes some time to finish. To test your code on smaller maps, use `count`:
```python
roads = load_map_from_csv(count=10000)
```

And you can add `start` argument to work in more "interesting" regions:
```python
roads = load_map_from_csv(start=100000, count=10000)
```

##Classes
###tl;dr
`Roads` is a mapping from integers (Junction index) to `Junction`, which has a list of `links` in it.
`Link_traffic_params` contains some deterministically-generated parameters for the `Link` speed history.

###Details
`Link`, `Junction` and `Link_traffic_params` are `namdetuple`
(https://docs.python.org/2/library/collections.html#collections.namedtuple) - which means they are tuple-like and immutable.

####`Junction`

* `index` : `int` Junction index
* `lat` : `float` Latitude
* `lon` : `float` Longitude
* `links` : `list(Link)`

####`Link`

* `source` : `int` Junction index
* `target` : `int` Junction index
* `distance` : `float` Meters
* `highway_type` : `int` See `info.py`
* `link_params`: `Namedtuple`

####`Link_traffic_params`
	Don't worry about it.

####`Roads`)
The graph is a dictionary mapping Junction index to `Junction`, with some additional methods.

This is the return type of `load_map_from_csv`.

#####Methods
All the methods for [`dict`](https://docs.python.org/2/library/stdtypes.html#mapping-types-dict) are available here too. For example, `roads[15]` is the Junction whose index is 15.

* `iterlinks(self) -> iterable(Link)`
   Chains all the links in the graph. ```for link in road.iterlinks(): ...```

* `junctions(self) -> list(Junction)`
   Iterate over the junctions in the road. Returns the values in the dictionary.

* `link_speed(self, link)`
   Returns the speed for the link (in km/h), based on  `self.generation`.

* `link_speed_history(self, link,time)`
   Returns the speed for the link (in km/h), based on some parameters which define the history of the traffic in the link at time `time` (in minutes, accepts non-integers)

* `realtime_link_speed(self, link)`
   Returns the speed for the link (in km/h), based on the history, time, and location (deterministically).


#####Fields

* `generation` : `int`

Represents the "sanpshot" of the speeds in the graph. This field is used by `link_speed` to decide the speed of a link for a specific generation.

   You can write and read freely to/from this field. 


* `base_traffic` : `list`

Represents some base traffic pattern which applies to all links: traffic peaks at ~8 and ~17. Do not modify.

* `mean_lat_lon` : `(float,float)`

Represents the mean latitude and longitude of the map.
You may change this field, but it would probably do more harm than good.
