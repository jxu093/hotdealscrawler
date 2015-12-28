from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/dev/sq3db.db'


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    url = db.Column(db.String, unique=False)

    def __init__(self, name, url):
        self.name = name
        self.url = url


@app.route('/')
def index():
    return 'hello'

if __name__ == '__main__':
    app.run()
