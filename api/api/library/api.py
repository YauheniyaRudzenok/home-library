from flask import request
from flask_restx import Resource

import os

from .dto import LibraryDto
from ..helpers import bad_request, created, deleted, not_found
from database.repositories.library_repository import LibraryRepository


api_ns = LibraryDto.api
_dto = LibraryDto.dto
_repository = LibraryRepository()


@api_ns.route("/")
class LibraryList(Resource):
    @api_ns.marshal_list_with(_dto)
    def get(self):
        return _repository.get_all()


    @api_ns.doc(responses = {
        201: 'Created', 
        400: 'Bad Request',
        404: 'Library does not found'})  
    @api_ns.expect(_dto)
    def post(self):
        if request.json:
            path = request.json["path"]
            root = os.path.abspath(os.sep)
            if path.startswith(root) is False:
                path = os.path.join(root, path)
            library = _repository.get_by_path(path)
            if library:
                return not_found()
            else:
                id = _repository.create(path)
                return created(id)
        else:
            return bad_request()


@api_ns.route("/<int:id>")
@api_ns.response(404, "Library not found")
@api_ns.param("id", "The library id")
class LibraryItem(Resource):
    @api_ns.doc("Delete library")
    @api_ns.response(204, "Library deleted")
    def delete(self, id):
        result = _repository.delete(id)
        return deleted(id) if result else not_found()