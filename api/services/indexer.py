import os

from .config_service import ConfigService
from .books_watcher import BooksWatcher
from .book_service import BookService
from database.repositories import LibraryRepository
from database.models import Library


class Indexer():
    types = (".fb2", ".txt", ".pdf", ".doc", ".docx",".mobi", ".epub", ".djvu")

    def __init__(self):
        self._config = ConfigService()
        self._library_repository = LibraryRepository()
        self._book_service = BookService()


    def start(self):
        libraries = self._library_repository.get_all()
        if(libraries is None):
            raise Exception('The libraries do not exists')
        self._index(libraries)
        self._watch(libraries)


    def start(self, lib_id: int):
        library = self._library_repository.get_by_id(lib_id)
        if library is None:
            raise Exception('The library does not exist')
        self._index(library)
        self._watch([library])


    def _index(self, libraries):
        if self._config.get_indexed(): return
        for library in libraries:
            self._index(library)
        self._config.set_indexed()


    def _index(self, library: Library):
        print('Indexing library: {path}'.format(path=library.path))
        for root, dirs, files in os.walk(library.path):
            for file in files:
                if file.endswith(self.types):
                    current_file = os.path.join(root, file)
                    self._book_service.add(current_file, library.id)
        print('Library index created')

    
    def _watch(self, libraries):
        patterns = []
        for pattern in self.types:
            patterns.append("*{pattern}".format(pattern=pattern))
        for library in libraries:
            BooksWatcher(library.path, patterns, library.id).start()