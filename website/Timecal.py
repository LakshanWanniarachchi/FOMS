
from datetime import datetime
import pytz
from sqlalchemy import desc


def calculate(orders):

    asia_colombo_tz = pytz.timezone('Asia/Colombo')

    time = []

    for order in orders:

        current_time = datetime.now(tz=asia_colombo_tz)

        End_date = order.date.astimezone(asia_colombo_tz)

        remain_time = End_date - current_time

        hours, remainder = divmod(remain_time.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)

        time.append({order.foid: {



            'date': remain_time.days,
            'hours': hours,
            'minutes': minutes,

        }})
    return time
