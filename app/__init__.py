from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()

db = SQLAlchemy()

def createApp():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:wx19931225@cdb-a67ycu2y.bj.tencentcdb.com:10123/personal'
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SECRET_KEY'] = 'MyBlog'
    db.init_app(app)
    from .main import main as main_blueprint
    from .user import user as user_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(user_blueprint)
    return app