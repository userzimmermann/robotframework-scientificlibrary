from matplotlib.pylab import *

from . import TestLibrary as _


@_.keyword
def compute(self, expression):
    return eval(expression, globals(), self.locals())
