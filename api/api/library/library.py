from flask import request
from flask_restx import Resource

from .library_dto import LibraryDto
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

    
    @api_ns.expect(_dto)
    @api_ns.marshal_with(_dto, code=201)
    def post(self):
        if request.json:
            path = request.json["path"]
            library = _repository.get_by_path(path)
            if library:
                return bad_request()
            else:
                _repository.create(path)
                return created()
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