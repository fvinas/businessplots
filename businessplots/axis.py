# -*- coding: utf-8 -*-

import matplotlib.ticker as mtick
import matplotlib.pyplot as plt

from . import formatters


# -----------------------
#    A convenient helper
# -----------------------
def xcoords(bar_length, this_bar_number=0, number_of_bars=1):
    bar_width = .5
    space_between_same_class_bars = .05
    space_between_classes = 1.3 * (number_of_bars * (bar_width + space_between_same_class_bars))

    return [j * space_between_classes + (this_bar_number + 1) * (bar_width + space_between_same_class_bars) for j in range(0, bar_length)]


# -----------------------
#    Helper functions
# -----------------------
def yaxis_to_percent(ax=None, **kwargs):
    """A helper to display y-axis 0 to 1 values as 0 to 100 percentages.

    Args:
        ax: Any relevant Axes object, defaults to current.
        **kwargs: Any dictionary of arguments, will be passed to the `formatters.tick_percent` tick formatter.

    Returns:
        None

    """
    if not ax:
        ax = plt.gca()
    ax.yaxis.set_major_formatter(mtick.FuncFormatter(formatters.tick_percent(**kwargs)))
    return None


def yaxis_to_unit(ax=None, **kwargs):
    """A helper to display y-axis values with a given number of decimals and a unit symbol.

    Args:
        ax: Any relevant Axes object, defaults to current.
        **kwargs: Any dictionary of arguments, will be passed to the `formatters.tick_value` tick formatter.

    Returns:
        None

    """
    if not ax:
        ax = plt.gca()
    ax.yaxis.set_major_formatter(mtick.FuncFormatter(formatters.tick_value(**kwargs)))
    return None


def yaxis_to_simplified(ax=None, **kwargs):
    """A helper to display y-axis as simplified values (e.g. 10k for 10.000) and a given unit.

    Args:
        ax: Any relevant Axes object, defaults to current.
        **kwargs: Any dictionary of arguments, will be passed to the `formatters.tick_simplified` tick formatter.

    Returns:
        None

    """
    if not ax:
        ax = plt.gca()
    ax.yaxis.set_major_formatter(mtick.FuncFormatter(formatters.tick_simplified(**kwargs)))
    return None
