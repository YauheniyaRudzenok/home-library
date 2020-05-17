import time
import os

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

import init
from .book_service import BookService


class BooksWatcher:
    def __init__(self, path: str, patterns: list, library_id: int):
        self._path = path
        self._event_handler = BooksEventHandler(patterns, library_id)
        self._event_observer = Observer()


    def start(self):
        self._schedule()
        self._event_observer.start()


    # def stop(self):
    #     self._event_observer.stop()
    #     self._event_observer.join()


    def _schedule(self):
        self._event_observer.schedule(
            self._event_handler,
            self._path,
            recursive=True
        )


class BooksEventHandler(PatternMatchingEventHandler):

    def __init__(self, patterns: list, library_id: int):
        self._library_id = library_id
        self._book_service = BookService()
        super().__init__(patterns=patterns, ignore_directories=True)


    def on_created(self, event):
        with init.create_app().app_context():
            self._book_service.add(event.src_path, self._library_id)


    def on_deleted(self, event):
        with init.create_app().app_context():
            self._book_service.delete(event.src_path)


    def on_moved(self, event):
        with init.create_app().app_context():
            self._book_service.moved(event.src_path, event.dest_path)