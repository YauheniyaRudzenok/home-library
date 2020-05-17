import os

from .goodreads import SearchBooks

from database.repositories import BookRepository


class BookService:
    def __init__(self):
        self._book_repository = BookRepository()


    def add(self, path: str, library_id: int):
        dir, file_name, title, ext = self._split_path(path)
        gr_book = self._search_book(title)
        goodreads_id = None
        if gr_book:
            title = gr_book.title()
            goodreads_id = gr_book.identifier()
        params = self._create_book_params(file_name, path, dir, library_id, title, goodreads_id)
        self._book_repository.create(**params)


    def delete(self, path: str):
        self._book_repository.delete(path)


    def moved(self, from_path: str, to_path: str):
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