from pushbullet import Pushbullet
from .models import FiverrOrder, SoundcloudTrack

from .Timecal import calculate

from flask import Blueprint


notification = Blueprint('notification', __name__)


def notificationSender():

    API_KEY = "o.9YbdrTpgYPfcRyKNxcbhiPEUI80e6Jxt"

    order = FiverrOrder.query.all()

    times  = calculate (order)


   
    pb = Pushbullet(API_KEY)
    

    push = pb.push_note("FOMS",times)

    









