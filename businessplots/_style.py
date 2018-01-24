# -*- coding: utf-8 -*-


def elevation(ax, elevation_factor=1.0):
    return .1 * elevation_factor * (ax.get_ylim()[1] - ax.get_ylim()[0])
