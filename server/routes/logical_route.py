# ? Группировка модулей
# Первая группа
import os
import datetime

# Вторая группа
# ? Импорт модулей в одну строчку
from flask import request, current_app, jsonify
from flask_restplus import Namespace, Resource
# ? Каждый импорт на отдельной строчке
# from flask import request
# from flask import current_app
# from flask_restplus import Namespace

# ? Третья группа модули внутри проекта
from ..db import get_db


api = Namespace('Test', path="/", description='Test route')


@api.route('/test/<string:identifier>/')
@api.response(200, "Success")
@api.response(400, "Couldn't add to DB")
class DevicePost(Resource):
    """ ?Комментарии для классов
    """
    def post(self, identifier: str):
        """ ? Комментарии для методов классов
        """

        storage = get_db()
        storage.execute("INSERT INTO test VALUES (?, ?)", (datetime.datetime.now(), identifier))
        storage.commit()
        return jsonify(text=identifier)


    @api.response(200, "Success")
    def get(self, identifier : str):
        """? Комментарии
        """
        storage = get_db()
        cursor = storage.cursor()
        cursor.execute("SELECT * FROM test WHERE text = ?", (identifier, ))
        return jsonify(res=cursor.fetchall())


