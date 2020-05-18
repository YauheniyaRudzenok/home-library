from flask_restx import Resource

from .dto import BookDto
from ..helpers import not_found
from database.repositories import BookRepository


api_ns = BookDto.api
_repository = BookRepository()


@api_ns.route("/<int:offset>/<int:count>")
@api_ns.param("offset", "The offset from the beginning")
@api_ns.param("count", "The count of returning books")
class BookList(Resource):
    @api_ns.marshal_list_with(BookDto.page)
    def get(self, offset:int, count:int):
        return _repository.get_list(offset, count)


@api_ns.route("/<int:id>")
@api_ns.response(404, "Book does not found")
@api_ns.param("id", "The book id")
class BookItem(Resource):
    @api_ns.doc("Book")
    @api_ns.response(200, "Book data")
    @api_ns.marshal_with(BookDto.book)
    def get(self, id):
        book = _repository.get_by_id(id)
        return book if book else not_found()