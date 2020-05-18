import os
import logging
import requests
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
            goodreads_id = None
            image_name = None
            if gr_book:
                image_name = self._download_image(gr_book.image_url(), dir, title)
                title = gr_book.title()
                goodreads_id = gr_book.identifier()
            params = self._create_book_params(file_name, path, dir, library_id, title, goodreads_id, image_name)
            self._book_repository.create(**params)
        except Exception as ex:
            self._logger.exception(ex)


    def delete(self, path: str):
        try:
            self._logger.info("Delete book {path}".format(path=path))
            book = self._book_repository.get_by_path(path)
            image_name = book.file.image_name
            image_path = book.file.path
            self._book_repository.delete(path)
            self._delete_image(image_path, image_name)
        except Exception as ex:
            self._logger.exception(ex)


    def moved(self, from_path: str, to_path: str):
        try:
            self._logger.info("Move book from {from_path} to {to_path}".format(from_path=from_path, to_path=to_path))
            dir, file_name, title, ext = self._split_path(to_path)
            book = self._book_repository.get_by_path(from_path)
            goodreads_id = book.goodreads_id
            image_name = book.file.image_name
            if goodreads_id is None:
                gr_book = self._search_book(title)
                if gr_book:
                    image_name = self._download_image(gr_book.image_url(), dir, title)
                    title = gr_book.title()
                    goodreads_id = gr_book.identifier()
            else:
                title = None
            params = self._create_book_params(file_name, to_path, dir, book.file.library_id, title, goodreads_id, image_name)
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
                            title: str, goodreads_id: int, image_name:str):
        return {
            "file_name": file_name,
            "full_path": path,
            "path": dir,
            "library_id": library_id,
            "title": title,
            "goodreads_id": goodreads_id,
            "image_name": image_name
        }


    def _download_image(self, url: str, path: str, name: str):
        url_path = urlparse(url).path
        ext = os.path.splitext(url_path)[1]
        image_name = "{name}{ext}".format(name=name, ext=ext)

        img_data = requests.get(url).content
        with open(os.path.join(path, image_name), 'wb') as handler:
            handler.write(img_data)

        return image_name


    def _delete_image(self, path:str, image_name:str):
        if image_name is None: return
        full_path = os.path.join(path, image_name)
        if os.path.exists(full_path):
            os.remove(full_path)
