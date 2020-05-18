import os
import logging

from .goodreads import SearchBooks
from database.repositories import BookRepository

import init


class BookService:
    def __init__(self):
        self._book_repository = BookRepository()
        self._logger = logging.getLogger()


    def add(self, path: str, library_id: int):
        try:
            self._logger.info("Add book {path}".format(path=path))
            dir, file_name, title, ext = self._split_path(path)
            gr_book = self._search_book(title)
            goodreads_id = None
            if gr_book:
                title = gr_book.title()
                goodreads_id = gr_book.identifier()
            params = self._create_book_params(file_name, path, dir, library_id, title, goodreads_id)
            self._book_repository.create(**params)
        except Exception as ex:
            self._logger.exception(ex)


    def delete(self, path: str):
        try:
            self._logger.info("Delete book {path}".format(path=path))
            self._book_repository.delete(path)
        except Exception as ex:
            self._logger.exception(ex)


    def moved(self, from_path: str, to_path: str):
        try:
            self._logger.info("Move book from {from_path} to {to_path}".format(from_path=from_path, to_path=to_path))
            dir, file_name, title, ext = self._split_path(to_path)
            book = self._book_repository.get_by_path(from_path)
            goodreads_id = book.goodreads_id
            if goodreads_id is None:
                gr_book = self._search_book(title)
                if gr_book:
                    title = gr_book.title()
                    goodreads_id = gr_book.identifier()
            else:
                title = None
            params = self._create_book_params(file_name, to_path, dir, book.file.library_id, title, goodreads_id)
            self._book_repository.update(book.id, **params)
        except Exception as ex:
            self._logger.exception(ex)


    def _split_path(self, path:str):
        dir, file_name = os.path.split(path)
        title, ext = os.path.splitext(file_name)
        return dir, file_name, title, ext


    def _search_book(self, title: str):
        gr_books = SearchBooks(title).books()
        return gr_books[0] if len(gr_books) > 0 else None


    def _create_book_params(self, file_name: str, path: str, dir: str, library_id: int, title: str, goodreads_id: int):
        return {
            "file_name": file_name,
            "full_path": path,
            "path": dir,
            "library_id": library_id,
            "title": title,
            "goodreads_id": goodreads_id
        }