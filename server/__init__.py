# ? Писать ли __version__, __author__ и т. д. на данном уровне
from typing import TypeVar


from flask import Flask
from flask import g


from .db import init_db
from .routes import api
from .types import ServerConfig


def init_app(config: TypeVar(ServerConfig)):
    """Init Flas app

    Args:
        config (ServerConfig): Config object

    Returns:
        Flask: instance of flask application
    """
    app = Flask(__name__)
    app.config.from_object(config)

    with app.app_context():
        init_db(app.config["DB_STORAGE_PATH"])
    # тут вроде должно быть два пустых пропуска
    @app.teardown_appcontext
    def close_connection(exception):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()

    api.init_app(app)

    return app
