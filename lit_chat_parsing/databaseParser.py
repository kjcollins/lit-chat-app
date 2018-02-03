"""
import stuff from Gutenberg database and make a dictionary of keywords, and the sentances theyb appear in

Femmehacks 2018
"""
import nltk
from nltk.book import *
nltk.corpus.gutenberg.fileids()

def makeDicts():
  """makes dictionary of shakespeare sentances word, sentence pairs"""
  caesar = nltk.corpus.gutenberg.sents('shakespeare-caesar.txt')
  hamlet = nltk.corpus.gutenberg.sents('shakespeare-hamlet.txt')
  macbeth = nltk.corpus.gutenberg.sents('shakespeare-macbeth.txt')

  shakespeare = {}
  for sent in caesar:
    for word in sent:
      if word.lower() in shakespeare.keys():
        shakespeare[word.lower()].append(" ".join(sent))
      else:
        
        shakespeare[word.lower()] = []
        shakespeare[word.lower()].append(" ".join(sent))

  for sent in hamlet:
    for word in sent:
      if word.lower() in shakespeare.keys():
        shakespeare[word.lower()].append(" ".join(sent))
      else:
    	  shakespeare[word.lower()] = []
    	  shakespeare[word.lower()].append(" ".join(sent))

  for sent in macbeth:
    for word in sent:
      if word.lower() in shakespeare.keys():
    	  shakespeare[word.lower()].append(" ".join(sent))
      else:
    	  shakespeare[word.lower()] =[]
    	  shakespeare[word.lower()].append(" ".join(sent))

  return shakespeare

def getSentence(keyword_list):
  """returns list of sentences containing given keyword"""  
  shakespeare = makeDicts()
  #print(keyword_list)
  list_ = []
  for keyword in keyword_list:
    if keyword in shakespeare.keys():
      #print('here')
      list_ += shakespeare[keyword]
      #print(list_)
      return list_
  else:
    return []

