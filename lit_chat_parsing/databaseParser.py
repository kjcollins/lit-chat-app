"""
import stuff from Gutenberg database and make a dictionary of keywords, and the sentances theyb appear in

Femmehacks 2018
"""
import nltk
# from nltk.book import *
nltk.corpus.gutenberg.fileids()
from .sentenceSentiment import sentimentOfSentence

def addPlay(dict_, play):
  for sent in play:
    sent_string = " ".join(sent)
    sentiment = 1 # sentimentOfSentence(sent_string)
    for word in sent:
      if word.lower() in dict_.keys():
        dict_[word.lower()].append((sentiment, sent_string))
      else:
        dict_[word.lower()] = []
        dict_[word.lower()].append((sentiment, sent_string))

def makeDicts():
  """makes dictionary of shakespeare sentances word, sentence pairs"""
  caesar = nltk.corpus.gutenberg.sents('shakespeare-caesar.txt')
  hamlet = nltk.corpus.gutenberg.sents('shakespeare-hamlet.txt')
  macbeth = nltk.corpus.gutenberg.sents('shakespeare-macbeth.txt')

  shakespeare = {}
  addPlay(shakespeare, caesar)

  addPlay(shakespeare, hamlet)

  addPlay(shakespeare, macbeth)

  return shakespeare

def getSentence(keyword_list, shakespeare):
  """returns list of sentences containing given keyword"""  
  #print(keyword_list)
  list_ = []
  for keyword in keyword_list:
    if keyword in shakespeare.keys():
      list_ += shakespeare[keyword]
      return list_
  else:
    return []

