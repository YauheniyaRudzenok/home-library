# temporary fix for 
# ImportError: cannot import name 'cached_property' from 'werkzeug'
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property

from flask_restplus import Api
from flask import Blueprint

from api.file_controller import api as file_ns

bp = Blueprint('api', __name__)

api = Api(bp,
          title='File api',
          version='1.0',
          description='the access to all books files'
          )

api.add_namespace(file_ns, path='/api/file')