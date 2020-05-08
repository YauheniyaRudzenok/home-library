from flask import Blueprint
from database.db import db
from services.indexer import Indexer


bp = Blueprint('commands', __name__)


@bp.cli.command('db_create')
def db_create():
    db.create_all()
    print('Database created!')


@bp.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('Database dropped!')


@bp.cli.command('index_files')
def index_files():
    Indexer().index()
    print('Indexed!')