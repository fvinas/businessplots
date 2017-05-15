# -*- encoding: utf-8 -*-

from matplotlib.patches import Ellipse

# TODO: add support for kwargs to customize text styles
def text(ax, x, y, text, kind='rect'):
	if kind == 'rect':
		text_artist = ax.text(x, y, text, fontsize=15, bbox=dict(fc='white', ec='k', pad=7), horizontalalignment='center', verticalalignment='center')
		bbox = text_artist.get_window_extent(ax.figure.canvas.get_renderer()).transformed(ax.transData.inverted())
		return bbox.height*2.5
	elif kind == 'ellipse':
		# a bit more complicated: we need to get the text width & height before adding the ellipse
		text_artist = ax.text(x, y, text, fontsize=15, horizontalalignment='center', verticalalignment='center', zorder=4)
		# get text bbox in axes coordinates (not in pixels)
		bbox = text_artist.get_window_extent(ax.figure.canvas.get_renderer()).transformed(ax.transData.inverted())
		ax.add_artist(Ellipse(xy=[x, y], width=bbox.width*1.8, height=bbox.height*2.5, angle=0, fc='white', zorder=3))
		return .5 * (bbox.height * 2.5)

