from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# from app import db

Base = declarative_base()
engine = create_engine('sqlite:////home/dev/sq3db.db')


class Thread(Base):
    __tablename__ = 'threads'

    id = Column(String, primary_key=True)
    title = Column(String)
    views = Column(Integer)
    url = Column(String)
    lastpostdate = Column(String)

    def __init__(self, id, title, views, url, lastpostdate):
        self.id = id
        self.title = title
        self.views = views
        self.url = url
        self.lastpostdate = lastpostdate


def init():
    engine = create_engine('sqlite:////home/dev/sq3db.db')
    Base.metadata.create_all(engine)


# class Thread(db.Model):
#     __tablename__ = 'threads'
#
#     id = db.Column(db.String, primary_key=True)
#     title = db.Column(db.String)
#     views = db.Column(db.Integer)
#     url = db.Column(db.String)
#     lastpostdate = db.Column(db.String)
#
#     def __init__(self, id, title, views, url, lastpostdate):
#         self.id = id
#         self.title = title
#         self.views = views
#         self.url = url
#         self.lastpostdate = lastpostdate

