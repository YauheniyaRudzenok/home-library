from flask_restx import Api
from flask import Blueprint

from .file.file import api as file_ns
from .library.library import api_ns as libray_ns


bp = Blueprint('api', __name__)

api = Api(bp,
          title='Home Library api',
          version='1.0',
          description='API contains all features for home library')

api.add_namespace(file_ns, path='/file')
api.add_namespace(libray_ns, path="/libraries")
