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

from __future__ import division

from six.moves import map, zip, zip_longest

import numpy as np
from pandas import Series
import matplotlib.pyplot as plt

from robottools import testlibrary

from BuiltIn import BuiltIn, RobotNotRunningError

from .utils import *


BUILTIN = BuiltIn()


TestLibrary = testlibrary()
keyword = TestLibrary.keyword


class ScientificLibrary(TestLibrary):

    def locals(self):
        try:
            return Locals(BUILTIN._variables)
        except RobotNotRunningError:
            return {}

    def array(self, data):
        if is_array(data):
            return data
        return np.array(list(map(self.compute, data)))

    @keyword
    def create_matrix(self, shape, *data):
        m, n = tuple(map(int, shape.split('x')))
        idata = map(self.compute, data)
        return np.mat(list(zip(*(m * [idata]))))

    @keyword
    def create_series(self, index, data):
        return Series(data=self.array(data), index=self.array(index))

    @keyword
    def plot(self, *args):
        plt.plot(*args)
        plt.show() #block=False)

    @keyword
    def plot_series(self, series, *args):
        plt.plot(series.index, series, *args)
        plt.show() #block=False)


from . import compute
