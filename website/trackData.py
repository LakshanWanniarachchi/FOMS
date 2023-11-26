
from flask import Blueprint, request, jsonify
from bs4 import BeautifulSoup
import requests

import json


trackData = Blueprint('trackData', __name__)


@trackData.route('/trackData', methods=['GET', 'POST'])
def return_track_data():

    url = request.json

    print(url)

    result = get_Soundcloud_track_data(url)

    return jsonify(result)


def get_Soundcloud_track_data(url):

    page = requests.get(url)

    respons = BeautifulSoup(page.text, 'html.parser')

    script_tags = respons.find_all('script')
    target_script = None

    for script in script_tags:
        if "likes_count" in str(script):
            target_script = script
            break

    text = target_script.text

    # Find the start of the JSON data
    json_data = text[text.index('[{'):-1]

    # Parse the JSON data

    data = json.loads(json_data)

    print(json.dumps(data, indent=2))

    # Access the "likes_count" field
    likes_count = int(data[-1]['data']['likes_count'])
    playback_count = int(data[-1]['data']['playback_count'])
    reposts_count = int(data[-1]['data']['reposts_count'])
    comment_count = int(data[-1]['data']['comment_count'])
    followers_count = int(data[-2]['data']['followers_count'])

    # Print the result
    # print("Likes Count:", likes_count)
    # print("Plays Count:", playback_count)
    # print("Repost Count:", reposts_count)
    # print("Comment Count:", comment_count)
    # print("Followers Count:", followers_count)

    result = [{

        'playback_count': playback_count,
        'likes_count': likes_count,
        'reposts_count': reposts_count,
        'comment_count': comment_count,
        'followers_count': followers_count


    }]

    return result
