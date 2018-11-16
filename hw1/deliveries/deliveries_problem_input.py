from framework.ways import Junction, Roads
from framework import Consts

from typing import FrozenSet, NamedTuple, List
import os


class DeliveriesProblemInput(NamedTuple):
    """
    This class is used to store and represent the input parameters
    to a deliveries-problem.
    It has a static method that may be used to load an input from a file. Usage example:
    >>> problem_input = DeliveriesProblemInput.load_from_file('big_delivery.in', roads)
    """

    input_name: str
    start_point: Junction
    drop_points: FrozenSet[Junction]
    gas_stations: FrozenSet[Junction]
    gas_tank_capacity: float
    gas_tank_init_fuel: float

    @staticmethod
    def load_from_file(input_file_name: str, roads: Roads) -> 'DeliveriesProblemInput':
        """
        Loads and parses a deliveries-problem-input from a file. Usage example:
        >>> problem_input = DeliveriesProblemInput.load_from_file('big_delivery.in', roads)
        """
        
        with open(Consts.get_data_file_path(input_file_name), 'r') as input_file:
            input_type = input_file.readline().strip()
            if input_type != 'DeliveriesProblemInput':
                raise ValueError('Input file `{}` is not a deliveries input.'.format(input_file_name))
            try:
                input_name = input_file.readline().strip()
                start_point = roads[int(input_file.readline())]
                drop_points = frozenset(roads[int(junc_idx.strip())] for junc_idx in input_file.readline().split(','))
                gas_stations = frozenset(roads[int(junc_idx.strip())] for junc_idx in input_file.readline().split(','))
                gas_tank_capacity = float(input_file.readline())
                gas_tank_init_fuel = float(input_file.readline())
            except:
                raise ValueError('Invalid input file `{}`.'.format(input_file_name))
        return DeliveriesProblemInput(input_name, start_point, drop_points, gas_stations, gas_tank_capacity, gas_tank_init_fuel)

    def store_to_file(self, input_file_name: str):
        with open(Consts.get_data_file_path(input_file_name), 'w') as input_file:
            lines = [
                'DeliveriesProblemInput',
                str(self.input_name.strip()),
                str(self.start_point.index),
                ', '.join(str(junction.index) for junction in self.drop_points),
                ', '.join(str(junction.index) for junction in self.gas_stations),
                str(self.gas_tank_capacity),
                str(self.gas_tank_init_fuel)
            ]
            for line in lines:
                input_file.write(line + '\n')

    @staticmethod
    def load_all_inputs(roads: Roads) -> List['DeliveriesProblemInput']:
        """
        Loads all the inputs in the inputs directory.
        :return: list of inputs.
        """
        inputs = []
        input_file_names = [f for f in os.listdir(Consts.DATA_PATH)
                            if os.path.isfile(os.path.join(Consts.DATA_PATH, f)) and f.split('.')[-1] == 'in']
        for input_file_name in input_file_names:
            try:
                problem_input = DeliveriesProblemInput.load_from_file(input_file_name, roads)
                inputs.append(problem_input)
            except:
                pass
        return inputs
