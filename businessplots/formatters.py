# -*- coding: utf-8 -*-

#
# Value formatters
# Formatters to display a single value
#

# TODO


#
# Delta formatters
# Formatters to display a delta between two values
#
def delta_percent(decimals=1):
    """A delta formatter to display the delta as a float with a given number of decimals.

    Args:
        decimals: The number of decimals to display.

    Returns:
        A delta formatter function (f(a,b)) returning (b-a)/a displayed as a percentage.

    """
    return (lambda a, b: '{:+.{prec}f}%'.format(100.0 * (b - a) / a, prec=decimals))


def delta_value(decimals=1, unit='$'):
    """A delta formatter to display the delta as a float with a given unit.

    Args:
        decimals: The number of decimals to display.
        unit: The unit symbol to display after the delta value.

    Returns:
        A delta formatter function (f(a,b)) returning (b-a)/a accompanied with a unit.

    """
    return (lambda a, b: '{:+,.{prec}f} {unit}'.format(1.0 * (b - a), unit=unit, prec=decimals))


def delta_simplified(decimals=1, unit='', prefixes=['k', 'M', 'B']):
    """A delta formatter to display the delta as a float with a given unit in a simplified way (e.g. 10k for 10.000)

    Args:
        decimals = 1: The number of decimals to display.
        unit = "": The unit symbol to concatenate to the value.
        prefixes = ['k', 'M', 'B']: The simplifier symbols to use for 1.000s, 1.000.000s and 1.000.000.000s.

    Returns:
        A delta formatter function (f(a,b)) returning (b-a)/a simplified and accompanied with a unit.

    """
    def formatter(a, b):
        delta = b - a
        prefix = ''
        if abs(delta) >= 1000000000:
            delta = delta * 1.0 / 1000000000
            prefix = prefixes[2]
        elif abs(delta) >= 1000000:
            delta = delta * 1.0 / 1000000
            prefix = prefixes[1]
        elif abs(delta) >= 1000:
            delta = delta * 1.0 / 1000
            prefix = prefixes[0]
        return '{:+,.{decimals}f} {prefix}{unit}'.format(1.0 * delta, decimals=decimals, prefix=prefix, unit=unit)
    return formatter


#
# Tick formatters
# Formatters to display axes ticks
# These formatters are designed to
#
def tick_percent(decimals=1):
    """A tick formatter to display the y-axis as a float percentage with a given number of decimals.

    Args:
        decimals = 1: The number of decimals to display.

    Returns:
        A tick formatter function (f(y, position)) displaying y as a percentage.

    """
    return (lambda y, position: '{:.{decimals}f}%'.format(100.0 * y, decimals=decimals))


def tick_value(decimals=1, unit=''):
    """A tick formatter to display the y-axis as a float value with a given unit symbol.

    Args:
        decimals = 1: The number of decimals to display.
        unit = "": The unit symbol to concatenate to the value.

    Returns:
        A tick formatter function (f(y, position)) displaying y as a float with a unit symbol.

    """
    return (lambda y, position: '{:+,.{decimals}f} {unit}'.format(1.0 * y, unit=unit, decimals=decimals))
    # def formatter(y, position):
    #    return "{:+,.{decimals}f} {unit}".format(1.0*y, unit=unit, decimals=decimals)
    # return formatter


def tick_simplified(decimals=1, unit='', prefixes=['k', 'M', 'B']):
    """A tick formatter to display the y-axis as a simplified value with a given unit symbol.

    Args:
        decimals = 1: The number of decimals to display.
        unit = "": The unit symbol to concatenate to the value.
        prefixes = ['k', 'M', 'B']: The simplifier symbols to use for 1.000s, 1.000.000s and 1.000.000.000s.

    Returns:
        A tick formatter function (f(y, position)) displaying y as a float with a simplified notation and a unit symbol.

    """
    def formatter(y, position):
        prefix = ''
        if abs(y) >= 1000000000:
            y = y * 1.0 / 1000000000
            prefix = prefixes[2]
        elif abs(y) >= 1000000:
            y = y * 1.0 / 1000000
            prefix = prefixes[1]
        elif abs(y) >= 1000:
            y = y * 1.0 / 1000
            prefix = prefixes[0]
        return '{:,.{decimals}f} {prefix}{unit}'.format(1.0 * y, decimals=decimals, prefix=prefix, unit=unit)
    return formatter
