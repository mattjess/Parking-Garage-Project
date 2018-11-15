import os
from twilio.rest import Client

print("When giving me a phone number please use the following formate")
print("+13171234567 (should look like that")
sendNum=input("Enter the phone number to send too: ")
sendMe=input("Enter what you want me to text")

account_sid =("AC5869a527aa268573dda13a43b20093a8")

auth_token =("bcc38465137e47f23254a76804e9a402")

client = Client(account_sid, auth_token)

client.messages.create(
	to=sendNum,
	from_="+13176718753",
	body=sendMe
	)