from ..models import Book, File
from ..db import db


class BookRepository:
    def __init__(self):
        self._db = db

    def create(self, **params):
        file, book = self._parse_params(**params)
        self._db.session.add(book)
        self._db.session.commit()


    def delete(self, file_path: str):
        session = self._db.session
        try:
            file = session.query(File).filter_by(full_path=file_path).first()
            if file is None:
                raise Exception("The file does not found {file}".format(file=file_path))
            book = session.query(Book).filter_by(id=file.book_id).first()
            session.delete(book)
            session.delete(file)
            session.commit()
        except Exception as ex:
            print(ex)
            session.rollback()
        finally:
            session.close()


    def get_by_path(self, path: str):
        return self._db.session.query(Book).join(File, Book.file).filter_by(full_path=path).first()


    def get_by_id(self, id: int):
        return self._db.session.query(Book).join(File, Book.file).filter(Book.id==id).first()

    
    def update(self, id: int, **params):
        file_data, book_data = self._parse_params(**params)
        book = self.get_by_id(id)
        if book is None:
            raise Exception("The book with id {id} doesn't find.".format(id=id))
        if book_data.title is not None:
            book.title = book_data.title
        book.goodreads_id = book_data.goodreads_id
        book.file.file_name = file_data.file_name
        book.file.path = file_data.path
        book.file.full_path = file_data.full_path
        self._db.session.commit()


    def _parse_params(self, **params):
        goodreads_id = params["goodreads_id"] if "goodreads_id" in params else None
        file = File(file_name = params["file_name"],
                    full_path = params["full_path"],
                    path = params["path"],
                    library_id = params["library_id"])
        book = Book(title = params["title"],
                    goodreads_id = goodreads_id,
                    file = file)
        return file, book