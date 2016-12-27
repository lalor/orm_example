from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
            "mysql://laimingxing:laimingxing@59.111.123.138/test"
db = SQLAlchemy(app)


class Student(db.Model):
    sno = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sname = db.Column(db.String(10))
    sage = db.Column(db.Integer)
    saddress= db.Column(db.String(50), nullable=True)

    def __init__(self, username, age, address):
        self.sname = username
        self.sage = age
        self.saddress = address

    def __repr__(self):
        return '{0}({1})'.format(self.__class__.__name__, self.__dict__)
