
from . import create_app

from math import e
from pushbullet import Pushbullet
from .models import FiverrOrder

from .Timecal import calculate








def notificationSender():
   
   

   
    
 
 app = create_app()

 

 with app.app_context():
    
   try:



    API_KEY = "o.jmI0eJwGDEJsJM4bUklor6Q98IoFPCIN"

    pb = Pushbullet(API_KEY)
     
     
     
     

    order = FiverrOrder.query.all()

    times  = calculate (order)
     
    print(times[1]['date'])


    push = pb.push_note("FOMS",str(times[1]['date']))
   


   except Exception as e:
   
     print(f"Error in notification_sender: {e}")

    







notificationSender()

