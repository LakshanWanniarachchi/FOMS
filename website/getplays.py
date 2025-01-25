
from requests import post
import json
from flask import Blueprint, request, flash,  redirect, url_for, render_template
from .views import home

import datetime
import time
import schedule

getplays = Blueprint('getplays', __name__)


@getplays.route('/get-plays', methods=['POST'])
def smm_plays():

    if request.method == 'POST':

        link = request.form.get("url")
        quantity = request.form.get("plays_count")
        foid = request.form.get("foid")

        # Define the API endpoint URL
        api_url = "https://www.smm-world.com/api/v1"

    # Define the required parameters
        api_key = "c292d86d5f7168f0cc32dce1c2904bcbc8722c12da4b5c9964f3af1fffee2f626bf46e2962af058c9608ba59efdff846"
        action = "add"
        service_id = 120


# Create the request payload
        payload = {
            "key": api_key,
            "action": action,
            "service": service_id,
            "link": link,
            "quantity": quantity

        }

# Send the POST request
        response = post(api_url, json=payload)

# Check the response
        if response.status_code == 200:

            # Request was successful, and you can parse the JSON response
            response_data = response.json()
            flash(
                f"The order has been placed ! order no:{response_data['order']}", category='success')
        else:
            # Request failed
            flash(f"error:{response_data['error']}", category='error')

        return redirect('/tracks?foid='+foid)

    else:
        return redirect(url_for("views.load_track"))




def  soundcloud_plays(track_url, plays_count):
    
    
    
    try: 
        # Define the API endpoint URL
        api_url = "https://www.smm-world.com/api/v1"

        # Define the required parameters
        api_key = "f8ee225c6586e296b7129d32b4be152663dedf6f3e713340c2d22e462bfd9f7a39f6ba9b4232c81782225a561fb30489"
        action = "add"
        service_id = 120
    
        # Create the request payload
        payload = {
            "key": api_key,
            "action": action,
            "service": service_id,
            "link": track_url,
            "quantity": plays_count
        }
    
        # Send the POST request
        response = post(api_url, json=payload)
    
        # Check the response
        if response is None:
            return 0
        else:
            response_data = response.json()
            if "order" in response_data:
                return 1
            else:
                return 0
    
    except Exception as e:
        return f"An error occurred: {e}"
    
    
    
    