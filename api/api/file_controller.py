from flask_restplus import Resource, Namespace, fields
from database.models import File


class FileDto:
    api = Namespace('file')
    file = api.model('file', {
        'id': fields.String(required=True),
        'file_name': fields.String(required=True),
        'path': fields.String(required=True)
    })


api = FileDto.api
_file = FileDto.file


@api.route('/')
class FileList(Resource):
    @api.marshal_list_with(_file, envelope='data')
    def get(self):
        return File.query.all()


