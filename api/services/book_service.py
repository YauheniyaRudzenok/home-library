import os
import logging
import requests
import base64
from urllib.parse import urlparse

from .goodreads import SearchBooks, Book
from database.repositories import BookRepository


class BookService:
    def __init__(self):
        self._book_repository = BookRepository()
        self._logger = logging.getLogger()


    def add(self, path: str, library_id: int):
        try:
            self._logger.info("Add book {path}".format(path=path))
            dir, file_name, title, ext = self._split_path(path)
            gr_book = self._search_book(title)
            params = self._create_book_params(
                file_name=file_name,
                full_path=path,
                path=dir,
                library_id=library_id,
                title=title)
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
            else:
                title = None
            params = self._create_book_params(
                file_name=file_name,
                full_path=to_path,
                path=dir,
                library_id=book.file.library_id,
                title=title)
            self._book_repository.update(book.id, **params)
        except Exception as ex:
            self._logger.exception(ex)

    
    def update(self, id: int, book):
        params = self._create_book_params(
            None,
            file_name=book.file.file_name,
            full_path=book.file.full_path,
            path=book.file.path,
            library_id=book.file.library_id,
            title=book.title,
            description=book.description,
            authors=book.authors,
            goodreads_id=book.goodreads_id)
        self._book_repository.update(book.id, **params)


    def _split_path(self, path:str):
        dir, file_name = os.path.split(path)
        title, ext = os.path.splitext(file_name)
        return dir, file_name, title, ext


    def _search_book(self, title: str):
        gr_books = SearchBooks(title).books()
        return gr_books[0] if len(gr_books) > 0 else None


    def _create_book_params(self, gr_book, **kwargs):
        """
        :param str file_name: The name of the book file
        :param str full_path: The full path to the book file
        :param str path: The path to the folder with book file
        :param int library_id: The identifier of the library for the book
        :param str title: The title of the book
        :param str description: The book description
        :param str authors: The authors of the book
        :param int goodreads_id: The identifier from goodreads.com
        """

        if gr_book:
            kwargs["title"] = gr_book.title()
            kwargs["goodreads_id"] = gr_book.id
            kwargs["description"] = gr_book.description()
            kwargs["authors"] = ', '.join(map(lambda x: x.name(), gr_book.authors()))
            kwargs["image"] = self._download_image(gr_book.image_url())

        return kwargs


    def _download_image(self, url: str):
        img_data = requests.get(url).content
        return base64.b64encode(img_data)
