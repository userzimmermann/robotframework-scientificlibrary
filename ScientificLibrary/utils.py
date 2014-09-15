__all__ = ['Locals', 'is_array_like', 'is_array']

import robot.utils
from robot.errors import DataError

import numpy as np


class Locals(object):
    def __init__(self, robot_vars):
        self.robot_vars = robot_vars

    def __getitem__(self, name):
        try:
            return self.robot_vars['${%s}' % name]
        except DataError:
            raise KeyError(name)


is_array_like = robot.utils.is_list_like


def is_array(obj):
    return isinstance(obj, np.ndarray)


def is_matrix(obj):
    return isinstance(obj, np.matrix)
