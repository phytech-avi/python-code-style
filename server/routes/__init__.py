from flask_restplus import Api

from .logical_route import api as test_api

api = Api(title='Test API', prefix='/api')
api.add_namespace(test_api)
