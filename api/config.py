from services.config_service import ConfigService


class Config(object):

    def __init__(self):
        config = ConfigService()
        self.SQLALCHEMY_DATABASE_URI = config.db_path()
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False