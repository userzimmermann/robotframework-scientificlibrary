# robotframework-scientificlibrary
#
# Copyright (C) 2014 Stefan Zimmermann <zimmermann.code@gmail.com>
#
# robotframework-scientificlibrary
# is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# robotframework-scientificlibrary
# is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with robotframework-scientificlibrary.
# If not, see <http://www.gnu.org/licenses/>.

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
