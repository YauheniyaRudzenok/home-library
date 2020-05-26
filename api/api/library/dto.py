from flask_restx import Namespace, fields

class LibraryDto:
    api = Namespace('libraries')
    dto = api.model('library', {
        'id': fields.String(),
        'path': fields.String(required=True)
    })