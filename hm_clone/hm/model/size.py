from hm import db


class Size(db.Model):
    __tablename__ = "size"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))

    def __init__(self, name):
        self.name = name
