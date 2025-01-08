from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import loginManager

db = SQLAlchemy
login_maneger = loginManager

def Creatin_app ():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sua_chave'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

    db.init_app(app)
    login_maneger.init_app(app)

    return app