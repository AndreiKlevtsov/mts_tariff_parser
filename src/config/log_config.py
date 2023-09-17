import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_FILE = os.path.join(BASE_DIR, "./django.log")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "main",
        },
        "file": {
            "level": "WARNING",
            "class": "logging.FileHandler",
            "filename": LOG_FILE,
            "formatter": "main",
        },
    },
    "formatters": {
        "main": {
            "format": "%(log_color)s%(asctime)s, %(levelname)s,"
                      " %(message)s, %(name)s, %(funcName)s,"
                      " %(lineno)d,",
            "()": "colorlog.ColoredFormatter",
        },
    },
    "loggers": {
        "": {
            "handlers": ["console", "file"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}
