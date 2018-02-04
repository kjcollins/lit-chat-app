# keyword parsing  

from google.cloud import language 

def processInput(msg):
	# if msg.lower() in ['hi', 'hello', 'what', 'good morning', 'howdy']:
	# 	return greeting_on_time()
	# else:
	# 	return msg
	pass

def retrieve_entities(text):
	client = language.LanguageServiceClient()
	document = language.types.Document(
		content=text,
		type=language.enums.Document.Type.PLAIN_TEXT
		)
	# response = client.analyze_entities(
	# 	document=document,
	# 	encoding_type='UTF32',
	# 	)
	tokens = client.analyze_syntax(document).tokens
	pos_tags = [1, 3, 6, 11]
	# pos_tags = ['ADJ', 'ADV', 'NOUN', 'VERB']

	print(tokens)
	ent_list = []
	for token in tokens:
		print(token.part_of_speech.tag)
		if token.part_of_speech.tag in pos_tags:
			ent_list.append(token.text.content)

	print(ent_list)
	# print(response.entities)
	# print(response.entities[0].name)
	
	# for entity in response.entities:
	# 	ent_list.append(entity.name)
	# print(ent_list)
	return ent_list #[entity.name for entity in response.entities]

def getKeyword(msg):
    #analyze entities thing 
    return retrieve_entities(msg)
	# return msg


