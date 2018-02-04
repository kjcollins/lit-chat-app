from google.cloud import language
client = language.LanguageServiceClient()
from random import choice

def chooseSentence(sent):
	# 'sent', is now a list of (score, sentence) pairs.
	if len(sent) >= 1:
		return choice(sent)[1]
	else:
		return ""
    # sentscore = 0
    # result = ""

    # for score, sent_item in sent:
    # 	if score >= score:
    # 		result = sent_item
    # return result


def sentimentOfSentence(item):
	document = language.types.Document(
	    content = item,
	    type = 'PLAIN_TEXT',
	    )
	response = client.analyze_sentiment(
	    document = document,
	    encoding_type='UTF32',
	    )
	sentiment = response.document_sentiment
	
	return sentiment.magnitude

