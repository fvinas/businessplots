# -*- coding: utf-8 -*-


def _data_from_bar(ax, bar_label):
    """Given a matplotlib Axes object and a bar label,
    returns (x,y,w,h) data underlying the bar plot.

    Args:
        ax: The Axes object the data will be extracted from.
        bar_label: The bar label from which you want to extract the data.

    Returns:
        A list of (x,y,w,h) for this bar.

    """

    data = []
    # each bar is made of several rectangles (matplotlib "artists")
    # here we extract their coordinates from the bar label

    handles = ax.get_legend_handles_labels()
    # handles[0] is a list of list of artists (one per bar)
    # handles[1] is a list of bar labels
    bar_artists = handles[0][handles[1].index(bar_label)]

    # each artist of the bar is a rectangle
    for rectangle in bar_artists:
        data.append([
            rectangle.get_x(),
            rectangle.get_y(),
            rectangle.get_width(),
            rectangle.get_height()
        ])

    return data
