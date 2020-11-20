import matplotlib.pyplot as plt
import cartopy.feature as cfeature
import numpy as np

from geocat.viz.util import add_major_minor_ticks
from geocat.viz.util import set_titles_and_labels
from geocat.viz.util import set_axes_limits_and_ticks

class NCL_Plot:

    # Constructor
    def __init__(self, *args, **kwargs):
        # Set class defaults
        self._default_height = 8
        self._default_width = 10

        # TODO: address input arguments
        # Pull out title arguments
        self.main_title = kwargs.get('main_title')
        self.left_title = kwargs.get('left_title')
        self.right_title = kwargs.get('right_title')

        # Pull out axes label arguments
        self.xlabel = kwargs.get('xlabel')
        self.ylabel = kwargs.get('ylabel')

        # Set up figure
        self._set_up_fig()


        # Set up axes
        if kwargs.get('projection') is not None:
            self.projection = kwargs.get('projection')
            self.ax = plt.axes(projection=self.projection)
            self.ax.coastlines(linewidths=0.5, alpha=0.6)
        else:
            self.ax = plt.axes()


        set_axes_limits_and_ticks(self.ax,
                                 xlim=(-180, 180),
                                 ylim=(-90, 90),
                                 xticks=np.linspace(-180, 180, 13),
                                 yticks=np.linspace(-90, 90, 7))
        
        self._set_NCL_style(self.ax)

        # Set specified features
        if kwargs.get('show_land') is True:
            self.show_land()

        if kwargs.get('show_coastline') is True:
            self.show_coastline()
        
        if kwargs.get('show_lakes') is True:
            self.show_lakes()

    def _set_up_fig(self, w=None, h=None):

        # Use default figure height and width if none provided
        if h is None:
            h = self._default_height

        if w is None:
            w = self._default_width

        self.fig = plt.figure(figsize=(w, h))

    def _set_NCL_style(self, ax):
        # Set NCL-style tick marks
        # TODO: switch from using geocat-viz to using a geocat-lynx specific tick function
        add_major_minor_ticks(ax, labelsize=10)

        # Set NLC-style titles set from from initialization call
        # TODO: switch from using geocat-viz to using a geocat-lynx specific title function
        set_titles_and_labels(ax, self.main_title, self.left_title, self.right_title, self.xlabel,
                              self.ylabel)

    def show_land(self, color='lightgrey'):
        self.ax.add_feature(cfeature.LAND, facecolor=color)

    def show_coastline(self, lw=0.5):
        self.ax.add_feature(cfeature.COASTLINE, linewidths=lw)
    
    def show_lakes(self, lw=0.5, ec='black', fc='None'):
        self.ax.add_feature(cfeature.LAKES,
               linewidth=lw,
               edgecolor=ec,
               facecolor=fc)

    def add_titles(self, main_title=None, left_title=None, right_title=None, xlabel=None, ylabel=None):
        set_titles_and_labels(self.ax, main_title, left_title, right_title, xlabel, ylabel)

    def show(self):
        plt.show()

    def get_mpl_obj(self):
        return self.fig

