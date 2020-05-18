import os
from distutils import util

from database.db import db
from database.models import Setting


class ConfigService():

    INDEXED_KEY = "indexed"


    def get_indexed(self):
        return bool(util.strtobool(self._get_settings(self.INDEXED_KEY, "False")))    


    def set_indexed(self):
        self._set_settings(self.INDEXED_KEY, True)


    def db_path(self):
        return 'sqlite:///' + os.path.join(self.base_path(), 'library.db')


    def base_path(self):
        return os.getcwd()
        

    def _get_settings(self, key, default):
        setting = Setting.query.filter_by(key=key).first()
        return setting.value if setting else default


    def _set_settings(self, key, value):
        setting = Setting.query.filter_by(key=key).first()
        if setting:
            setting.value = value
        else:
            setting = Setting(key = key, value = value)
            db.session.add(setting)
        db.session.commit()