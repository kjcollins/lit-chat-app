# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.twiml.messaging_response import Message, MessagingResponse
from flask import Flask, request, redirect
from twilio.rest import Client
from twilio import twiml
from nltk.corpus import gutenberg
from lit_chat_parsing import * # getKeyword, getSentence, chooseSentence
#from databaseParser import *
def parseUserMessage(msg):
	clean_msg = keywordParse.processInput(msg)
	keyword = keywordParse.getKeyword(clean_msg)
	list_ = databaseParser.getSentence(keyword)
	to_respond = sentenceSentiment.chooseSentence(list_)
	if to_respond == "":
		return "Sorry but Shakespeare can't hang"
	else:
	    return to_respond

	# if "hi" == msg:
	# 	response.message('Holla!')
	# elif "hello" == msg:
	# 	response.message("Stand, ho!")
	# else:
	# 	response.message(inputHandler(msg))

app = Flask(__name__)
@app.route('/sms', methods=['GET', 'POST'])

def sms():
	msg = request.form.get('Body').lower().strip() # gets incoming message
	
	resp = MessagingResponse()
	
	# based on incoming message, send different message
	to_respond = parseUserMessage(msg)

	resp.message(to_respond)
	
	#return message: if you just want to send any message, return this
	return str(resp)

if __name__ == "__main__":
	app.run(debug=True)
