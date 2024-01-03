from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from .models import FiverrOrder, SoundcloudTrack
from . import db

from .trackData import get_Soundcloud_track_data

from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import requests
import pytz
from .Timecal import calculate


from sqlalchemy import desc

views = Blueprint('views', __name__)


@views.route('/')
def home():

    return render_template("Home.html")


@views.route('/from-load', methods=['GET', 'POST'])
def for_load():

    if request.method == 'POST':

        acount_name = request.form.get("account")
        fiverr_order_number = request.form.get("Fiverr_Oder_Number")
        Soundcloud_url = request.form.get("url")
        Hours = int(request.form.get("hours"))
        Minutes = int(request.form.get("minutes"))
        Days = int(request.form.get("days"))
        status = request.form.get("OderStatus")

        delta = timedelta(days=Days, hours=Hours, minutes=Minutes)

        End_Date = datetime.now()+delta

        # tz=pytz.timezone('Asia/Colombo')

        print(End_Date)

        track_data = get_Soundcloud_track_data(Soundcloud_url)

        plays = track_data[0]['playback_count']
        likes = track_data[0]['likes_count']
        repost = track_data[0]['reposts_count']
        comments = track_data[0]['comment_count']
        followers = track_data[0]['followers_count']

        new_data = FiverrOrder(fono=fiverr_order_number,
                               account_name=acount_name, date=End_Date,status=status)

        print(End_Date)
        # print(datetime.strptime(End_Date, '%Y-%m-%d').date())

        db.session.add(new_data)

        db.session.commit()

        # Order_no = FiverrOrder.query.filter_by(
        #     fono=fiverr_order_number).first()

        print(new_data.foid)
        new_track = SoundcloudTrack(soundcloud_track=Soundcloud_url, plays=plays,
                                    likes=likes, repost=repost,  comments=comments, followers=followers)

        new_track.foid = new_data.foid

        db.session.add(new_track)
        db.session.commit()

        flash('Track add success',  category='success')

        # order_id = 1
        # fiverr_order = FiverrOrder.query.get(order_id)

        # if fiverr_order:
        #     print(
        #         f"Fiverr Order ID: {fiverr_order.foid}, Order Number: {fiverr_order.foNo}, Account Name: {fiverr_order.account_name}, Date: {fiverr_order.date}")
        #     for track in fiverr_order.soundcloud_tracks:
        #         print(
        #             f"Soundcloud Track ID: {track.track_id}, URL: {track.url}")
        # else:
        #     print(f"Fiverr Order with ID {order_id} not found.")

        return redirect(url_for("views.home"))
    else:
        return redirect(url_for("views.home"))


@views.route('/order')
def order():

    account_name = 'Jayanthi'  # Replace with the account_name you want to query
    # orders = FiverrOrder.query.filter_by(account_name=account_name).all()

    orders = FiverrOrder.query.order_by(desc(FiverrOrder.foid)).all()

    time = calculate(orders)

    # for order in orders:

    #     print(
    #         f"Fiverr Order ID: {order.foid},Account name : {order.account_name} Fono: {order.fono}, Date: {order.date}")

    #     # Convert the list of orders to a JSON response
    # orders_json = [{
    #     order.foid:
    #     {
    #         'foid': order.foid,
    #         'account_name': order.account_name,
    #         'fono': order.fono,
    #         # Format the date as a string
    #         'date': order.date.strftime('%Y-%m-%d')
    #     }
    #     for order in orders
    # }]

    # jsonify(orders_json)

    return render_template('Activeorder.html', orders=orders, time=time)


@views.route('/tracks', methods=['GET', 'POST'])
def load_track():

    if request.method == 'GET':
        foid = request.args.get('foid', '')

        # orders = FiverrOrder.query.filter_by(foid=foid).all()

        soundcloud_track = SoundcloudTrack.query.filter_by(
            foid=foid).all()
        
        order  = FiverrOrder.query.filter_by(
            foid=foid).all()

        return render_template('tracks.html', tracks=soundcloud_track , order = order)
    return render_template('tracks.html')


@views.route('/Jayanthi')
def jayanthi_order_load():

    account_name = 'Jayanthi'  # Replace with the account_name you want to query
    orders = FiverrOrder.query.filter_by(
        account_name=account_name).order_by(desc(FiverrOrder.foid)).all()

    time = calculate(orders)

    # asia_colombo_tz = pytz.timezone('Asia/Colombo')

    # time = []

    # for order in orders:

    #     current_time = datetime.now(tz=asia_colombo_tz)

    #     End_date = order.date.astimezone(asia_colombo_tz)

    #     remain_time = End_date - current_time

    #     hours, remainder = divmod(remain_time.seconds, 3600)
    #     minutes, seconds = divmod(remainder, 60)

    #     print(remain_time.days, hours, minutes)

    return render_template("jayanthi.html", orders=orders, time=time)


@views.route('/Sajith')
def sajith_order_load():

    account_name = 'Sajith'  # Replace with the account_name you want to query
    orders = FiverrOrder.query.filter_by(
        account_name=account_name).order_by(desc(FiverrOrder.foid)).all()

    # .order_by(desc(FiverrOrder.foid))

    time = calculate(orders)

    return render_template("Sajith.html", orders=orders, time=time)


@views.route('/Ishara')
def Ishara_order_load():

    account_name = 'Ishara'  # Replace with the account_name you want to query
    orders = FiverrOrder.query.filter_by(
        account_name=account_name).order_by(desc(FiverrOrder.foid)).all()

    # .order_by(desc(FiverrOrder.foid))

    time = calculate(orders)

    return render_template("Ishara.html", orders=orders, time=time)


@views.route('/delete', methods=['POST'])
def track_data_delete():

    if request.method == 'POST':

        foid = request.form.get("foid")
        redirect_page = request.form.get("redirect_page")

        soundcloud_track = SoundcloudTrack.query.filter_by(
            foid=foid).first()

        db.session.delete(soundcloud_track)
        db.session.commit()

        track_data = FiverrOrder.query.filter_by(
            foid=foid).first()

        db.session.delete(track_data)
        db.session.commit()

        print('done')

        return redirect('/'+redirect_page)
    

@views.route('/oderstatus',methods=['POST'] )
def oderstatus():

     if request.method == 'POST':
         
          foid = request.form.get("foid") 

          orderstatus = request.form.get("orderstatus")


          order = FiverrOrder.query.filter_by(
            foid=foid).first()
          
          order.status = orderstatus

          db.session.commit()

          return redirect('/tracks?foid='+foid)







         



