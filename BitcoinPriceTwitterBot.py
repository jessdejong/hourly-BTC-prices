from twython import Twython
from exchanges import coindesk
import datetime

from auth import (
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)
twitter = Twython(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

now = datetime.datetime.now()

message = now.strftime("%Y-%m-%d %I:%M") + " Bitcoin Price: " + str(round(coindesk.CoinDesk.get_current_price(), 2)) + " USD"

#twitter.update_status(status=message)
print("Tweeted: {}".format(message))
