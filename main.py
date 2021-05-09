from twilio.rest import Client
from decouple import config

account_sid = 'ACb1141044b5119773d54deb292463bf0d'
auth_token = config('auth_token')
client = Client(account_sid, auth_token)


def send_message():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Hi papa',
        to='whatsapp:' + config('target_no')
    )

    print(message.sid)
