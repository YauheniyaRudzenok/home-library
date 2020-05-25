from flask_restx import Namespace, fields

class FileManagerDto:
    api = Namespace('fm')
    folder = api.model('folder', {
        'path': fields.String,
        'folders': fields.List(fields.String, description='folders', required=True)
    })