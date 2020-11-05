import os
import datetime
from flask_sqlalchemy import SQLAlchemy

DATABASE_URL = os.getenv("DATABASE_URL")
db = SQLAlchemy()


def setup_db(app, database_path=DATABASE_URL):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app=app)


def drop_and_create_all():
    db.drop_all()
    db.create_all()


class Table(db.Model):
    __tablename__ = "table"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name, created_at=None):
        self.name = name
        self.created_at = created_at

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return ({
            "id": self.id,
            "name": self.name,
            "created_at": datetime.datetime.strftime(self.created_at, '%Y-%m-%d %H:%M:%S.%f')
        })
