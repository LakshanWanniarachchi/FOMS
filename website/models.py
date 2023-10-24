from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
import pytz
from datetime import datetime


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    fiverr_order = db.relationship('fiverr_order')


class fiverr_order(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    oid = db.Column(db.Integer, primary_key=True)

    def current_date_time_in_sri_lanka():
        srilanka_tz = pytz.timezone('Asia/Colombo')
        current_time = datetime.now(tz=srilanka_tz)
        return current_time

    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # print(current_date_time_in_sri_lanka())
