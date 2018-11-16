# -*- coding: utf-8 -*-

from time import clock
import zlib
from math import acos, radians, pi
from numpy import ones, cos, array, sin

'General tools'

'This is arbitrary, and will change in the tests'
SEED = 0x23587643


def dhash(*data):
    'Generates a random-looking deterministic hash'
    return abs(zlib.adler32(bytes(str(data), 'UTF-8')) * 100) * SEED % 0xffffffff


## The move from python 2 to 3 caused some problems.


'DMS := Degrees, Minutes, Seconds'


def float2dms(decimal_degrees):
    degrees = int(decimal_degrees)
    minutes = int(60 * (decimal_degrees - degrees))
    seconds = int(3600 * (decimal_degrees - degrees - minutes / 60))
    return (degrees, minutes, seconds)


def dms2float(degrees, minutes, seconds=0):
    return degrees + minutes / 60 + seconds / 3600


def compute_distance(pnt1, pnt2):
    '''computes distance in Meters'''
    '''
    This code was borrowed from 
    http://www.johndcook.com/python_longitude_latitude.html
    '''

    lat1, lon1 = pnt1
    lat2, lon2 = pnt2

    if (lat1, lon1) == (lat2, lon2):
        return 0.0
    if max(abs(lat1 - lat2), abs(lon1 - lon2)) < 0.00001:
        return 0.001

    phi1 = radians(90 - lat1)
    phi2 = radians(90 - lat2)

    meter_units_factor = 40000 / (2 * pi)
    arc = acos(sin(phi1) * sin(phi2) * cos(radians(lon1) - radians(lon2))
               + cos(phi1) * cos(phi2))
    return arc * meter_units_factor  * 1000


def base_traffic_pattern():
    ''' Creates a base traffic pattern:
            we can go at max speed (divide by 1)
            traffic gets worse at 6 AM and 3 PM, with peak at 8 AM and 5 PM, 
            and then it subsides again within 2 hours'''

    base_pattern = ones(60 * 24)
    base_pattern[(60 * 6):(10 * 60)] += cos(((array(range(4 * 60)) / (4 * 60)) - 0.5) * pi)
    base_pattern[(15 * 60):(19 * 60)] += base_pattern[(60 * 6):(10 * 60)]
    return list(base_pattern)


def generate_traffic_noise_params(seed1, seed2):
    ''' generates some parameters for the traffic noise
    It should look random, and it is symmetrical
    (Can't think why it has to be symmetrical, but it would be easy enough to
    modify it not to be if need be) '''
    wavelength_cos = 60 + 20 * (dhash(seed1 + seed2) / 0xffffffff) - 10
    wavelength_sin = 60 + 20 * (dhash(seed1 * seed2) / 0xffffffff) - 10
    return (wavelength_cos, wavelength_sin)
    ## should It only be positive addition to the multiplier? A* needs an optimistic hueristic


def timed(f):
    '''decorator for printing the timing of functions
    usage: 
    @timed
    def some_funcion(args...):'''

    def wrap(*x, **d):
        start = clock()
        res = f(*x, **d)
        print("{}: {:.2f}sec".format(f.__name__, clock() - start))
        return res

    return wrap


if __name__ == '__main__':
    for i in range(100):
        print(dhash(i))
