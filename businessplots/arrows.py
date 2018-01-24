# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

from . import _data
from . import _text
from . import _style
from . import _limits
from . import _overlap

from . import formatters
from . import axis


reload(_data)
reload(_text)
reload(_style)
reload(_limits)
reload(_overlap)
reload(formatters)
reload(axis)


def increase_arrow(
        ax=None,
        bar_from='',
        bar_to='',
        index_from=0,
        index_to=-1,
        format_func=None,
        automatic_elevation=True,
        elevation_factor=1.0,
        text_kind='ellipse',
        arrow_kind='tendancy'):
    """Adds value increase arrows to a bar plot.

    Args:
        ax (Axes): Any relevant Axes object. Defaults to `plt.gca()` (current Axes).
        bar_from (string): The bar label from which the arrow will start. Defaults to the last added bar.
        bar_to (string): The bar label to which to the arrow will end. Defaults to bar_from.
        index_from (int): The class index from which the arrow will start (i.e. the index_from-th occurence on the x-axis). Defaults to 0 (first point).
        index_to (int): The class index to which the arrow will end (i.e. the index_to-th occurence on the x-axis). Defaults to -1 (last point).
        format_func (function): The value formatter function to use. Defaults to `formatters.delta_percent(1)`.
        automatic_elevation (bool): If True, businessplots computes the text box elevation so that it doesn't overlap with another existing plot. Defaults to True.
        elevation_factor (float): Elevation factor that will be applied to compute the y position of the text box. Defaults to 1.0.
        text_kind (text): Type of text box. Can be an ellipse ('ellipse') or a rectangle ('rect'). Defaults to 'ellipse'.
        arrow_kind (text): Type of arrow. Can be a tendancy-like ('tendancy') or more vertical ('delta'). Defaults to 'tendancy'.

    Returns:
        None

    """

    # take last bar added by default
    if not ax:
        ax = plt.gca()
    if bar_from == '':
        bar_from = ax.get_legend_handles_labels()[1][-1]
    if bar_to == '':
        bar_to = bar_from
    if format_func is None:
        format_func = formatters.delta_percent(1)
    data_from = _data._data_from_bar(ax, bar_from)
    data_to = _data._data_from_bar(ax, bar_to)
    bar_width = data_from[0][2]

    if arrow_kind == 'tendancy':
        arrow_start_x = data_from[index_from][0] + .5 * bar_width
        arrow_start_y = data_from[index_from][3] + _style.elevation(ax, elevation_factor)
        arrow_end_x = data_to[index_to][0] + .5 * bar_width
        arrow_end_y = data_to[index_to][3] + _style.elevation(ax, elevation_factor)
        if automatic_elevation:
            arrow_start_x, arrow_start_y, arrow_end_x, arrow_end_y = _overlap.adjust_elevation(ax, arrow_start_x, arrow_start_y, arrow_end_x, arrow_end_y, _style.elevation(ax, elevation_factor))

        ax.annotate('', xy=(arrow_end_x, arrow_end_y), xytext=(arrow_start_x, arrow_start_y), arrowprops=dict(arrowstyle='-|>', linewidth=1))
        text_height = _text.text(ax, .5 * (arrow_start_x + arrow_end_x), .5 * (arrow_start_y + arrow_end_y), format_func(data_from[index_from][3], data_to[index_to][3]), kind=text_kind)

        # Adjust limits in case we go out of the plot
        _limits.adjust_limits(ax, arrow_start_y)
        _limits.adjust_limits(ax, arrow_end_y)

    elif arrow_kind == 'delta':
        ymin, ymax = ax.get_ylim()
        xmin, xmax = ax.get_xlim()
        arrow_head_length = .02 * (ymax - ymin)
        arrow_head_width = .01 * (xmax - xmin)
        text_elevation = _style.elevation(ax, elevation_factor)
        line_elevation = 0.1 * _style.elevation(ax, elevation_factor)

        text_font_size = 15

        x1 = data_from[index_from][0]
        y1 = data_from[index_from][3]
        x2 = data_to[index_to][0]
        y2 = data_to[index_to][3]

        delta = y2 - y1
        height = max(0, delta)
        diff = 1.2
        arrow_height = y1 - y2 + height

        x1 += .5 * bar_width
        x2 += .5 * bar_width

        plot_color = 'black'

        top_y = y1 + height + text_elevation + line_elevation

        if automatic_elevation:
            text_height = 2.5 * (ax.transData.inverted().transform((0, text_font_size)) - ax.transData.inverted().transform((0,0)))[1]
            _, _, _, top_y = _overlap.adjust_elevation(ax, x1 + (x2 - x1) * .5, top_y - text_height, x1 + (x2 - x1) * .5, top_y, text_elevation)

        # First vertical line
        ax.plot([x1, x1], [y1 + line_elevation, top_y], color=plot_color, linestyle='-', linewidth=1, alpha=1)
        # Horizontal line
        ax.plot([x1, x2], [top_y, top_y], color=plot_color, linestyle='-', linewidth=1, alpha=1)
        # Second vertical line = arrow
        ax.arrow(x2, top_y, 0, y2 + line_elevation - top_y + arrow_head_length, head_width=arrow_head_width, head_length=arrow_head_length, linewidth=1, color=plot_color, alpha=.8)
        # Horizontal text
        text_height = _text.text(ax, x1 + (x2 - x1) * .5, top_y, format_func(y1, y2), kind=text_kind)

        # Adjust limits in case we go out of the plot
        _limits.adjust_limits(ax, top_y + text_height)

    return None
