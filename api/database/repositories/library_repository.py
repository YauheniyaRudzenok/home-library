from ..models import Library
from ..db import db

class LibraryRepository():
    def get_all(self):
        return Library.query.all()


    def get_by_path(self, path: str):
        return Library.query.filter_by(path=path).first()


    def get_by_id(self, id: int):
        return Library.query.filter_by(id=id).first()

    
    def create(self, path: str):
        library = Library(path = path)
        db.session.add(library)
        db.session.commit()
        return library.id


    def delete(self, id:int):
        library = Library.query.filter_by(id=id).first()
        if(library is None): return False
        db.session.delete(library)
        db.session.commit()
        return True

