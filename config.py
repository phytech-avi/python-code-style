"""? Комментарий вначале модуля
"""

import os
import pathlib


class Config:
    """Комментарий для классов?
    """
    DEBUG = False
    DB_STORAGE_PATH = os.path.join("storage", "db_storage.sqlite")


class BaseConfig(Config):
    """ Base Run Config
    """
    BUG = False


class TestConfig:
    """Description for what context this config
    """
    DEBUG = True
    DB_STORAGE_PATH = "test/db_storage.sqlite"
