from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/dev/sq3db.db'


# class Url(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), unique=True)
#     url = db.Column(db.String, unique=False)
#
#     def __init__(self, name, url):
#         self.name = name
#         self.url = url


class Thread(db.Model):
    __tablename__ = 'threads'

    id = db.Column(db.String, primary_key=True)
    title = db.Column(db.String)
    views = db.Column(db.Integer)
    url = db.Column(db.String)
    lastpostdate = db.Column(db.String)

    def __init__(self, id, title, views, url, lastpostdate):
        self.id = id
        self.title = title
        self.views = views
        self.url = url
        self.lastpostdate = lastpostdate


@app.route('/')
def index():
    return 'hello'

if __name__ == '__main__':
    app.run()
