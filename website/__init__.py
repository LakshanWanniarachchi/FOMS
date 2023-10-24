from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path


db = SQLAlchemy()
DB_NAME = 'FOMS.db'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Lakshan'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .models import User, fiverr_order

    with app.app_context():

        db.create_all()

    return app
