from twilio.rest import Client

account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "your_auth_token"

client = Client(account_sid, auth_token)

def send_sms_verification(phone_number):
    message = client.messages.create(
        body="Your verification code is 123456",
        from_="+1XXXXXXXXXX",  #  Twilio
        to=phone_number
    )
    print("SMS sent:", message.sid)

# 
send_sms_verification("+213XXXXXXXX")
