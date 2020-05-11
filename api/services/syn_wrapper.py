from synology_api import filestation
from services.config_service import ConfigService


class SynologyWrapper():
    

    def __init__(self):
        self._config = ConfigService()
        #self._fl = filestation.FileStation()
        self._fl = filestation.FileStation(self._config.ds_ip(), self._config.ds_port(), self._config.ds_user(), self._config.ds_password())


    def get_library_folder(self):
        shares = self._fl.get_list_share()["data"]["shares"]
        filtered=list(filter(lambda f: f["path"] == self._config.library_path(), shares))
        folder_data=next(iter(filtered), None)
        return folder_data["path"] if folder_data is not None else None


    def start_searching(self, folder):
        self._fl.search_start(folder, True, extension="fb2", filetype="file")
        return self._fl._search_taskid


    def stop_searching(self, taskid):
        self._fl.stop_search_task(taskid)


    def get_search_result(self, taskid, offset, limit):
        response = self._fl.get_search_list(taskid, limit=limit, offset=offset)
        return response["data"] if response["data"] is not None else []