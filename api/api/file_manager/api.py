from flask_restx import Resource, reqparse
import os

from .dto import FileManagerDto

api_ns = FileManagerDto.api

@api_ns.route("/")
class FileManagerList(Resource):
    @api_ns.marshal_list_with(FileManagerDto.folder)
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('path', type=str, help='The path on the server')
        args = parser.parse_args()
        path = args.path
        if path is None:
            path = os.sep
        else:
            path = os.path.join(os.sep, path)
        abspath = os.path.abspath(path)
        list = []
        [list.append(name) for name in os.listdir(path)
            if os.path.isdir(os.path.join(path, name))]
        return {
            "path": path,
            "folders": list
        }