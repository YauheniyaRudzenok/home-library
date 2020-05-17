import os

from .config_service import ConfigService
from .books_watcher import BooksWatcher
from .book_service import BookService
from database.repositories import LibraryRepository


class Indexer():
    types = (".fb2", ".txt", ".pdf", ".doc", ".docx",".mobi", ".epub", ".djvu")

    def __init__(self):
        self._config = ConfigService()
        self._library_repository = LibraryRepository()
        self._book_service = BookService()


    def start(self):
        libraries = self._library_repository.get_all()
        if(libraries is None):
            raise Exception('The libraries do not set')
        self._index(libraries)
        self._watch(libraries)


    def _index(self, libraries):
        if self._config.get_indexed(): return
        print('Indexing library')
        for library in libraries:
            for root, dirs, files in os.walk(library.path):
                for file in files:
                    if file.endswith(self.types):
                        current_file = os.path.join(root, file)
                        self._process_file(current_file, library.id)
        self._config.set_indexed()
        print('Library index created')


    def _process_file(self, input:str, lib_id: int):
        self._book_service.add(input, lib_id)

    
    def _watch(self, libraries):
        patterns = []
        for pattern in self.types:
            patterns.append("*{pattern}".format(pattern=pattern))
        for library in libraries:
            BooksWatcher(library.path, patterns, library.id).start()