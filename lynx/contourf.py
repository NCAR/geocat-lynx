"""Plotting wrapper for matplotlib contourf function."""

import matplotlib.pyplot as plt
import warnings
import numpy as np
import cartopy.crs as ccrs


from _plot_util import NCL_Plot

class Contour(NCL_Plot):
    # child class constructor
    def  __init__(self, *args, **kwargs):

        # set class defaults
        self._default_cmap = 'coolwarm'

        # Pull out args
        self.data = args[0]

        # Read in or calculate filled levels
        if kwargs.get('flevels') is not None:
            # levels defined by kwargs
            self.levels = kwargs.get('flevels')
        else:
            # take a guess at filled levels
            self._estimate_flevels

        # Pull out child-class specific kwargs
        if kwargs.get('cmap') is not None:
            self.cmap = kwargs.get('cmap')
        else:
            self.cmap = self._default_cmap

        # Call parent class constructor
        NCL_Plot.__init__(self, *args, **kwargs)

        if kwargs.get('contour_fill') is not False:
            plt.contour(self.data)



