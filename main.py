"""Main app module."""

# -- Imports

import logging
from log import conf_logging, foo

# --

log = logging.getLogger(__name__)

# --


def main():
    conf_logging(level=logging.INFO)
    foo()


if __name__ == "__main__":
    main()
