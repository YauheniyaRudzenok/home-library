import os


class ConfigService():

    def ds_ip(self):
        return self.__env_or_default__('HL_DS_IP', '127.0.0.1')


    def ds_port(self):
        return self.__env_or_default__('HL_DS_PORT', 5000)


    def ds_user(self):
        return self.__env_or_default__('HL_DS_USER', 'admin')


    def ds_password(self):
        return os.environ.get('HL_DS_USER_PASSWORD')


    def library_path(self):
        return os.environ.get('HL_PATH')


    def db_path(self):
        return 'sqlite:///' + os.path.join(self.base_path(), 'library.db')


    def base_path(self):
        return os.getcwd()


    def __env_or_default__(self, key, default):
        value=os.environ.get(key)
        return value if value is not None else default