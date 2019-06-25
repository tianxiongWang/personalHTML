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
    discusses = db.relationship('Discuss', backref='user', lazy = 'dynamic')


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
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Cate(db.Model):
    __tablename__ = 'cate'
    id =  db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    pictures = db.relationship('Picture', backref = 'cate', lazy = 'dynamic')
    path = db.Column(db.String(50), nullable=False)


class Picture(db.Model):
    __tablename__ = 'picture'
    id =  db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    cate_id = db.Column(db.Integer, db.ForeignKey('cate.id'))
    path = db.Column(db.String(150), nullable=False)
    static = db.Column(db.String(150), nullable=False)