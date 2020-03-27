# Группировка import
# ? Первая группа
import sqlite3
import os

# ? Вторая группа
from flask import current_app
from flask import g

# ALL указываем в том случае если наш module не зависит от внешних модулей, и не важно положение в FS OS
# это поможет создать из этого module -> pakage
# ? Писать ли all
__all__ = ["get_db", "init_db"]

# Все переменные, которые не должны экспортироваться начинать с _
_PATH_TO_STORAGE = None

# Функция которая не должна использоваться снаружи модуля
# Начинается с нижнего подчёркивания


def _create_dir(path_to_file: str) -> None:
    """Private module db function to create dir if not exists

    Args:
        path_to_file (str): fs path to file
    """
    dir_name = os.path.dirname(path_to_file)

    if not os.path.exists(dir_name):
        os.makedirs(dir_name, exist_ok=True)


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        if _PATH_TO_STORAGE is None:
            raise ValueError()
        db = g._database = sqlite3.connect(_PATH_TO_STORAGE)
    return db

# Подсказки типов указываем обязательно внутри module даст хорошее понимание при прочтении


def init_db(path_to_storage: str) -> None:
    """Function wich inits database location

    Args:
        path_to_storage (str): FS path to sqlite file
    """
    global _PATH_TO_STORAGE
    _PATH_TO_STORAGE = path_to_storage

    _create_dir(_PATH_TO_STORAGE)

    storage = sqlite3.connect(_PATH_TO_STORAGE)
    storage.execute("""CREATE TABLE IF NOT EXISTS test (date, text)""")
    storage.commit()
    storage.close()
