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
