# -*- encoding: utf-8 -*-

import matplotlib.pyplot as plt

def pretty_title(ax = None, message = '', description = ''):
	"""Adds a pretty title to the axes with a message and a description.

	Args:
	    ax: The Axes object you want to put the title on, defaults to current.
	    message: A headline with the business interpretation of the plot (e.g. "Amazon revenues more than doubled in the last 4 years")
	    description: A short description of what's plotted (e.g. "Amazon revenues from 2012 to 2016")

	Returns:
	    The title object (a Text artist)

	"""
	if not message and not description:
		return None
	if not ax:
		ax = plt.gca()
	# TODO: find a correct way to do this (esp. the Axes margin part)
	ax.set_title("\n{}\n\n".format(message), fontsize=18)
	ax.text(0.5, 1, "— {} —\n\n\n".format(description), fontsize=14, transform=ax.transAxes, ha='center', va='center')
