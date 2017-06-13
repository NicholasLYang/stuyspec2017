from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % (self.name)

class Article(db.Model):
    title = db.Column(db.String(256), index=True, unique=False)
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    section = db.Column(db.String(64), index=True, unique=False) # this data type needs to be better

    def __repr__(self):
        return '<Article %r>' % (self.body)
