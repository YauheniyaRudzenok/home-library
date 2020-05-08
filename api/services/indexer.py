from services.syn_wrapper import SynologyWrapper
from database.db import db
from database.models import File


class Indexer():

    def __init__(self):
        self._wrapper = SynologyWrapper()
        self._db = db


    def index(self):
        folder = self._wrapper.get_library_folder()
        if(folder is None):
            raise Exception('The library folder does not find')
        taskid = self._wrapper.start_searching(folder)
        self.process_files(taskid, 0, 20)
        self._wrapper.stop_searching(taskid)


    def process_files(self, taskid, offset, limit):
        response = self._wrapper.get_search_result(taskid, offset, limit)
        for fl in response["files"]:
            file = File(file_name=fl["name"],
                        path=fl["path"])
            self._db.session.add(file)
            offset += 1
        self._db.session.commit()
        if(response["finished"] == True and response["total"] <= offset):
            return
        else:
            self.process_files(taskid, offset, limit)
            