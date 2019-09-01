# -*- coding: utf-8 -*-

"""The main module"""

#
# Standard imports
#
import logging.config

#
# Project's imports
#
import enigma.helpers

logger = logging.getLogger("enigma")


def main():
    """The main function

    """
    enigma.helpers.configure_logging(gmt=True)


if __name__ == "__main__":
    main()
