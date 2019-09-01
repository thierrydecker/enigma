# -*- coding: utf-8 -*-

"""The helpers module"""

import logging
import logging.config
import time

logger = logging.getLogger("enigma.helpers")


def configure_logging(gmt=True):
    """Configure logging

    Args:
        gmt: GMT flag for log records timestamps

    Returns: None

    """
    logging.config.dictConfig(
            {
                "version": 1,
                "formatters": {
                    "detailed": {
                        "class": "logging.Formatter",
                        "style": "{",
                        "format":
                            "[{asctime}]"
                            " [{levelname:8s}]"
                            " [{levelno}]"
                            " - {message}"
                            " - {processName}"
                            " ({process})"
                            " - {threadName}"
                            " ({thread})"
                            " - {name}"
                            " - {pathname}"
                            " - {filename}"
                            " - {module}"
                            " - {funcName}"
                            " - {lineno}"
                    },
                    "compacted": {
                        "class": "logging.Formatter",
                        "style": "{",
                        "format":
                            "[{asctime}]"
                            " [{levelname:8s}]"
                            " - {message}"
                    },
                },
                "handlers": {
                    "console": {
                        "class": "logging.StreamHandler",
                        "level": "DEBUG",
                        "formatter": "detailed",
                    },
                    "file": {
                        "class": "logging.FileHandler",
                        "filename": "logs/enigma.log",
                        "mode": "w",
                        "level": "DEBUG",
                        "formatter": "detailed",
                    },
                    "errors": {
                        "class": "logging.FileHandler",
                        "filename": "logs/enigma-errors.log",
                        "mode": "w",
                        "level": "ERROR",
                        "formatter": "detailed",
                    },
                },
                "loggers": {
                    "enigma": {
                        "level": "DEBUG",
                        "handlers": ["console", "file"],
                    }
                }
            }
    )
    if gmt is True:
        logging.Formatter.converter = time.gmtime
        logger.info("Logger timestamps switched to GMT")
    logger.info("Logger succesfuly configured")
