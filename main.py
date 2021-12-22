import os
from twilio.rest import Client
from dotenv import load_dotenv

# adding twilio credentials
load_dotenv()
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

call = client.calls.create(
    url='http://demo.twilio.com/docs/voice.xml',
    to='+14047218853',
    from_='+17089984068'
)

