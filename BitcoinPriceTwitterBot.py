from twython import Twython
from exchanges import coindesk

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
message = "Current Bitcoin Price: " + str(round(coindesk.CoinDesk.get_current_price(), 2)) + " USD"

#twitter.update_status(status=message)
print("Tweeted: {}".format(message))
