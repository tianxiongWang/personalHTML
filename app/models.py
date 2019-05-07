# 模型创建的模块
from . import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    phonenum = db.Column(db.String(30), nullable=False)
    boards = db.relationship('Board', backref='user', lazy='dynamic')


class Board(db.Model):
    __tablename__ = 'board'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    text = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    categoryName = db.Column(db.String(30), nullable=False)
    topics = db.relationship('Topic', backref='category', lazy='dynamic')


class Topic(db.Model):
    __tablename__ = 'topic'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    tittle = db.Column(db.String(30), nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    discusses = db.relationship('Discuss', backref='topic', lazy='dynamic')


class Discuss(db.Model):
    __tablename__ = 'discuss'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    time = db.Column(db.DateTime, nullable=False)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'))