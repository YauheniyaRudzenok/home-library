from flask_restx import Api
from flask import Blueprint

from .file_manager.api import api_ns as fm_ns
from .library.api import api_ns as libray_ns
from .books.api import api_ns as book_ns


bp = Blueprint('api', __name__)

api = Api(bp,
          title='Home Library api',
          version='1.0',
          description='API contains all features for home library')

api.add_namespace(fm_ns, path="/fm")
api.add_namespace(libray_ns, path="/libraries")
api.add_namespace(book_ns, path="/books")
