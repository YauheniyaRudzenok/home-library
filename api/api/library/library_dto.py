from flask_restx import Namespace, fields

class LibraryDto:
    api = Namespace('library')
    dto = api.model('library', {
        'id': fields.String(required=True),
        'path': fields.String(required=True)
    })