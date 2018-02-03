# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, redirect
from twilio.rest import Client
# from twilio import twiml




app = Flask(__name__)
@app.route('/sms', methods=['GET', 'POST'])

def sms():
	msg = request.form['Body'].lower() #gets incoming message
	if msg == "hi": #based on incoming message, send different message
		resp = MessagingResponse().message("Holla!")
	else:
		resp = MessagingResponse().message("Stand, ho!")
	#return message: if you just want to send any message, return this
	return str(resp)

if __name__ == "__main__":
	app.run(debug=True)

# response = MessagingResponse()
# response.message('Store Location: 123 Easy St.')

# print(response)


# for num in client.api.account.messages.list('+16572206721'):
# 	client.api.account.calls.create(
# 		to=num,
# 		from_='+16572206721',
# 		url = 'http://demo.twilio.com/docs/classic.mp3'
# 		)


# Find these values at https://twilio.com/user/account
# account_sid = 
# auth_token = 

# client = Client(account_sid, auth_token)
# client.api.account.messages.create(
#     to="",
#     from_="",
#     body="Hello there!")