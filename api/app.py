from flask import Flask, jsonify
from flask_cors import CORS

from config import Config
from database.db import db

import commands
import api


app = Flask(__name__)
CORS(app)
app.config.from_object(Config())
app.register_blueprint(commands.bp)
app.register_blueprint(api.bp)
db.init_app(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50000)