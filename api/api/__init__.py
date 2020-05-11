from flask_restx import Api
from flask import Blueprint

from api.file_controller import api as file_ns

bp = Blueprint('file', __name__)

api = Api(bp,
          title='File api',
          version='1.0',
          description='the access to all books files'
          )

api.add_namespace(file_ns, path='/file')