# keyword parsing  

from google.cloud import language 
import googleapiclient.discovery

def processInput(msg):
	return msg

def analyze_entities_1(text, encoding = 'UTF32'):
	body={
	 'document' : {
	   'type': 'PLAIN_TEXT',
	   'content' : text, 
	 },
	 'encoding_type' : encoding,
	}

	service = googleapiclient.discovery.build('language', 'v1')
	request = service.documents().analyzeEntities(body=body)
	response = request.execute()
	return response

def analyze_entities_2(text):
	client = language.LanguageServiceClient()
	document = language.types.Document(
		content=text,
		type=language.enums.Document.Type.PLAIN_TEXT
		)
	response = client.analyze_entities(
		document=document,
		encoding_type='UTF32',
		)
	# print(response.entities)
	# print(response.entities[0].name)
	ent_list = []
	for entity in response.entities:
		ent_list.append(entity.name)
	print(ent_list)
	return ent_list #[entity.name for entity in response.entities]

def getKeyword(msg):
    #analyze entities thing 
    return analyze_entities_2(msg)
	# return msg


