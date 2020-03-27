"""Configuration for this server
"""

import os
import pathlib


from server.types import ServerConfig


class Config(ServerConfig):
    """Main Config Gets K, V
         V - From Environment Varaibles By The Name of K
    """
    DEBUG = os.environ.get("PROJECT_DEBUG", False) == "True"
    DB_STORAGE_PATH = os.environ.get(
        "DB_STORAGE_PATH",  os.path.join("storage", "db_storage.sqlite"))


class DebugConfig(Config):
    """Debug Config
    """
    DEBUG = True


class DevConfig(Config):
    """Development Config
     Varaibles need for development server
    """
    DEBUG = True
    HOST = "localhost"
    PORT = 5000


class TestConfig(Config):
    """This Config only for UnitTests
    """
    DEBUG = True
    DB_STORAGE_PATH = "test/db_storage.sqlite"
