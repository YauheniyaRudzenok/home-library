import os
import logging
import requests
import base64
from urllib.parse import urlparse

from .goodreads import SearchBooks
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
            image = None
            if gr_book:
                image = self._download_image(gr_book.image_url())
            params = self._create_book_params(file_name, path, dir, library_id, title, image, gr_book)
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
            image = book.file.image
            if goodreads_id is None:
                gr_book = self._search_book(title)
                if gr_book:
                    image = self._download_image(gr_book.image_url())
            else:
                title = None
            params = self._create_book_params(file_name, to_path, dir, book.file.library_id, title, image, gr_book)
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


    def _create_book_params(self, file_name: str, path: str, dir: str, library_id: int, 
                            title: str, image:str, gr_book):
        goodreads_id = None
        description = None
        authors = None

        if (gr_book):
            title = gr_book.title()
            goodreads_id = gr_book.id
            description = gr_book.description()
            authors = ', '.join(map(lambda x: x.name(), gr_book.authors()))

        return {
            "file_name": file_name,
            "full_path": path,
            "path": dir,
            "library_id": library_id,
            "title": title,
            "goodreads_id": goodreads_id,
            "image": image,
            "description": description,
            "authors" : authors
        }


    def _download_image(self, url: str):
        img_data = requests.get(url).content
        return base64.b64encode(img_data)
