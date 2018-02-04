from google.cloud import language
client = language.LangaugeServiceClient()

def chooseSentence(sent){
    sentscore = 0
    result = ""
    for item in sent:
      doceument = langauge.types.Document(
        content = item
        type = 'PLAIN_TEXT',
      )
      response = client.analyze_sentiment(
        document = document,
        encoding_type='UTF32',
      )
      sentiment = response.document_sentiment
      if sentiment.magnitude >= sentscore:
        result = item;
    return result

      #print(sentiment.score)
      #print(sentiment.magntiude)


}

