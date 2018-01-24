# -*- coding: utf-8 -*-

from matplotlib.patches import Rectangle


def is_overlapping(ax, x, y):
    """An internal method to check whether a given (x,y) point overlaps any `Artist` of `Axes` `ax`.

    Args:
        ax: Any relevant Axes object.
        x, y: x coordinates of the point

    Returns:
        bool: `True` if an `Artist` overlaps the point, else `False`.

    """

    # Point (x,y) from user to display coordinates
    point_display = ax.transData.transform((x, y))

    for artist in ax.get_children():
        # Exclude any axes-wide rectangle (background)
        if isinstance(artist, Rectangle):
            if artist.get_x() == 0 and artist.get_y() == 0 and artist.get_width() == 1.0 and artist.get_height() == 1.0:
                continue
        if 'contains_point' in dir(artist):
            if artist.contains_point(point_display):
                # Debug
                # print("Overlap found with {}".format(artist))
                return True
    return False


def adjust_elevation(ax, x1, y1, x2, y2, step_y):
    """A helper to adjust a shape elevation when its center is overlapping existing objects.
    Works internally by testing the current position against potential overlapping,
    then increasing its y position step by step until it stop overlapping.

    Args:
        ax: Any relevant Axes object.
        x1, y1: Bottom-left coordinates of the shape.
        x2, y2: Top-right coordinates of the shape.
        step_y: The y-axis step to use to move the shape up and avoid overlapping.

    Returns:
        x1, y1, x2, y2: new bottom-left and top-right coordinates for the shape, with no overlapping.

    Raises:
        Exception: When the number of test loops is larger than 1.000 (something is going wrong).

    """

    nb_loops = 0
    while True:
        nb_loops += 1
        if nb_loops > 1000:
            raise Exception('Too many loops while testing objects overlapping')
        if not is_overlapping(ax, .5 * (x1 + x2), .5 * (y1 + y2)):
            break
        y1 += step_y
        y2 += step_y

    return x1, y1, x2, y2
