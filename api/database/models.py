from sqlalchemy import Column, Integer, String
from database.db import db


class File(db.Model):
    __tablename__ = 'files'
    id = Column(Integer, primary_key=True)
    file_name=Column(String)
    path=Column(String)