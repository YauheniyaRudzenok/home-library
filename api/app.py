from flask import Flask
from config import Config
from database.db import db
from services.indexer import Indexer

import commands
import api


app = Flask(__name__)
app.config.from_object(Config())
app.register_blueprint(commands.bp)
app.register_blueprint(api.bp)
db.init_app(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50000)