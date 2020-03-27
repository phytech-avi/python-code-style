# ? Писать ли __version__, __author__ и т. д. на данном уровне
from flask import Flask
from flask import g
from config import Config


from .db import init_db
from .routes import api

app = Flask(__name__)
app.config.from_object(Config)

with app.app_context():
    init_db(app.config["DB_STORAGE_PATH"])
# тут вроде должно быть два пустых пропуска
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


api.init_app(app)
