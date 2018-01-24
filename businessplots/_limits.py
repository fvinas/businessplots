# -*- coding: utf-8 -*-

PADDING_Y_COEFFICIENT = .05
PADDING_X_COEFFICIENT = .05


def padding_y(ax):
    """A helper returning the y-axis padding that should be used when defining the axes y-axis limits.
    This padding is 5% of the present height of the y-axis, in User coordinates.

    Args:
        ax: Any relevant Axes object.

    Returns:
        float: The padding to use.
    """
    return PADDING_Y_COEFFICIENT * (ax.get_ylim()[1] - ax.get_ylim()[0])


def padding_x(ax):
    """A helper returning the x-axis padding that should be used when defining the x-axis limits.
    This padding is 5% of the present height of the y-axis, in User coordinates.

    Args:
        ax: Any relevant Axes object.

    Returns:
        float: The padding to use.
    """
    return PADDING_X_COEFFICIENT * (ax.get_xlim()[1] - ax.get_xlim()[0])


def adjust_limits(ax, new_artist_top_y):
    """A helper to automatically adjust the top limit of the y-axis when a new Artist comes in.
    It basically tests if the current top y limit is fine, then if not it increases it to a right value.

    TODO: add other limits (bottom y, top & bottom x)

    Args:
        ax: Any relevant Axes object.
        new_artist_top_y: Top y coordinate of the new Artist.

    Returns:
        None
    """
    ylim = ax.get_ylim()
    if ylim[1] < (new_artist_top_y + padding_y(ax)):
        ax.set_ylim([ylim[0], new_artist_top_y + padding_y(ax)])
    return None
