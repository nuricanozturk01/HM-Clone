import json

from hm import db


class Image(db.Model):
    __tablename__ = "image"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return json.dumps({'id': self.id, 'name': self.name})
