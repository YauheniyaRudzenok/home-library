from flask_restx import Resource
from flask import request

from munch import Munch

from .dto import BookDto
from api.helpers import not_found, no_content, bad_request, ok
from database.repositories import BookRepository
from services.book_service import BookService


api_ns = BookDto.api
_repository = BookRepository()
_service = BookService()


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
        
    
    @api_ns.doc("Book")
    @api_ns.response(204, "Book updated")
    @api_ns.expect(BookDto.book)
    def put(self, id):
        if request.json:
            book = Munch(request.json)
            book.file = Munch(book.file)
            _service.update(id, book)
            return no_content()
        else:
            return bad_request()


    @api_ns.doc("Delete book")
    @api_ns.response(204, "Book deleted")
    def delete(self, id):
        result = _service.delete_by_id(id)
        return ok(id) if result else not_found()