from twilio.rest import Client

account_sid = "AC5869a527aa268573dda13a43b20093a8"
auth_token = "bcc38465137e47f23254a76804e9a402"
client = Client(account_sid, auth_token)

call = client.calls.create(
    to="+14155551212",
    from_="+15017250604",
    url="http://demo.twilio.com/docs/voice.xml"
)

print(call.sid)