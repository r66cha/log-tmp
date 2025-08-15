"""Template for logging example."""

# -- Imports

import logging
from time import sleep

# -- Exports

__all__ = ["foo"]

# --

log = logging.getLogger(__name__)

name = "John"
age = 20
cash = 45.16
speed = 37.456


# --


# %s string
# %r represented
# %d integer
# %f float %.2f


def expensive_foo():
    sleep(2)
    return 100


def foo():
    log.warning("Name: %s, Name repr: %r", name, name)
    log.warning("Age: %s, Age int: %d", age, age)
    log.warning("Cash: %s, Cash float: %f", cash, cash)
    log.warning("Speed: %s, Speed 2float: %.2f", speed, speed)

    if log.isEnabledFor(logging.INFO):
        log.info("Month cash: %s", expensive_foo())
