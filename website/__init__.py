from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from os import path


db = SQLAlchemy()
DB_NAME = 'FOMS.db'


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Lakshan'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .trackData import trackData
    from .getplays import getplays
    from apscheduler.schedulers.background import BackgroundScheduler
    from .notification import notificationSender
    
    scheduler = BackgroundScheduler()

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(trackData, url_prefix='/')
    app.register_blueprint(getplays, url_prefix='/')
    

    from .models import SoundcloudTrack, FiverrOrder
   

    with app.app_context():
        db.create_all()
        
        scheduler.add_job(notificationSender, 'interval', seconds=30)
        scheduler.start()
        


    return app
