from flask import Flask
from flask_cors import CORS

from config import Config
from database.db import db

import commands
import api

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(Config())
    app.register_blueprint(commands.bp)
    app.register_blueprint(api.bp)

    with app.app_context():
        db.init_app(app)

    return app