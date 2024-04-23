import json

from hm.extensions import db


class Color(db.Model):
    __tablename__ = "color"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return json.dumps({'id': self.id, 'name': self.name})
