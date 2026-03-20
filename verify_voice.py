from twilio.rest import Client

account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "your_auth_token"

client = Client(account_sid, auth_token)

def make_voice_call(phone_number):
    call = client.calls.create(
        twiml='<Response><Say>Your verification code is 123456</Say></Response>',
        to=phone_number,
        from_="+1XXXXXXXXXX"  # رقم Twilio
    )
    print("Call initiated:", call.sid)

# مثال
make_voice_call("+213XXXXXXXX")
