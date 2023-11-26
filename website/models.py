# from . import db
# from sqlalchemy.sql import func
# import pytz
# from datetime import datetime


# class SoundcloudTtracks(db.Model):

#     track_id = db.Column(db.Integer, primary_key=True)
#     url = db.Column(db.String(255))
#     foid = db.Column(db.Integer, db.ForeignKey('FiverrOrder.foid'))


# class FiverrOrder(db.Model):
#     foid = db.Column(db.Integer, primary_key=True)
#     foNo = db.Column(db.String(150), unique=True)
#     account_name = db.Column(db.String(150))
#     date = db.Column(db.DateTime(timezone=True), default=func.now())
#     Soundcloud_tracks = db.relationship('SoundcloudTtracks')

#     # def current_date_time_in_sri_lanka():
#     #     srilanka_tz = pytz.timezone('Asia/Colombo')
#     #     current_time = datetime.now(tz=srilanka_tz)
#     #     return current_time

#     # print(current_date_time_in_sri_lanka())


from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime
from . import db


class FiverrOrder(db.Model):
    foid = db.Column(db.Integer, primary_key=True)
    fono = db.Column(db.String, nullable=False)
    account_name = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    soundcloud_tracks = db.relationship(
        'SoundcloudTrack', backref='fiverr_order', lazy='dynamic')


class SoundcloudTrack(db.Model):
    soundcloud_id = db.Column(db.Integer, primary_key=True)
    soundcloud_track = db.Column(db.String, nullable=False)
    plays = db.Column(db.Integer)
    likes = db.Column(db.Integer)
    repost = db.Column(db.Integer)
    comments = db.Column(db.Integer)
    followers = db.Column(db.Integer)

    foid = db.Column(db.Integer, db.ForeignKey('fiverr_order.foid'))
