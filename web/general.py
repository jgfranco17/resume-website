"""
--- GENERAL.PY ---
This File serves as the storage for the general-purpose module of
various Python scripts and functions for the purpose of simplifying
the classes.
"""

import datetime

months_list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
colors = {
    'Red': "#FF96BA",
    'Blue': "#ABDEE6",
    'Yellow': "#FFFFB5",
    'Green': "#B6CFB6",
    'Orange': "#FFCA82",
    'Purple': "#ECD5E3"
}


def percent_diff(expected, actual) -> float:
    sign = 1 if expected > actual else -1
    value = (abs(actual-expected)/((actual+expected)/2)) * 100
    return sign * round(value, 2)


def min_max_change(minimum, maximum, base_value) -> dict:
    return {
        'minimum': percent_diff(minimum, base_value),
        'maximum': percent_diff(maximum, base_value)
    }


def timeformat(time_value) -> dict:
    return {
        'second': time_value.strftime("%d %B %Y, %I:%M:%S %p"),
        'minute': time_value.strftime("%d %B %Y, %I:%M %p"),
        'day': time_value.strftime("%d %B %Y"),
        'month': time_value.strftime("%B %Y"),
        'year': time_value.strftime("%Y")
    }


def timestamp() -> dict:
    return timeformat(datetime.datetime.utcnow())
