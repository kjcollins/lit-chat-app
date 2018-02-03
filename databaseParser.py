"""
import stuff from Gutenberg database and make a dictionary of keywords, and the sentances theyb appear in

Femmehacks 2018
"""
import nltk
from nltk.book import *
nltk.corpus.gutenberg.fileids()

def makeDicts():
  caesar = nltk.corpus.gutenberg.sents('shakespeare-caesar.txt')
  hamlet = nltk.corpus.gutenberg.sents('shakespeare-hamlet.txt')
  macbeth = nltk.corpus.gutenberg.sents('shakespeare-macbeth.txt')

  shakespeare = {}
  for sent in caesar:
    for word in sent:
      #if len(word) >= 5:
        l= list(shakespeare.keys())
	if word in l:
          shakespeare[word].append(" ".join(sent))
	else:
	  shakespeare[word] = []	  
	  shakespeare[word].append(" ".join(sent))

  for sent in hamlet:
    for word in sent:
     # if len(word) >= 5:
        l= list(shakespeare.keys())
        if word in l:
          shakespeare[word].append(" ".join(sent))
        else:
	  shakespeare[word] = []
	  shakespeare[word].append(" ".join(sent))

  for sent in macbeth:
    for word in sent:
      #if len(word)>= 5:
        l= list(shakespeare.keys())
        if word in l:
      	  shakespeare[word].append(" ".join(sent))
	else:
	  shakespeare[word] =[]
	  shakespeare[word].append(" ".join(sent))

  return shakespeare

def getSentance(keyword):
  shakespeare = makeDicts()
  #keyword = raw_input("input keyword: ")
  l = list(shakespeare.keys())
  if keyword in l:
    lsit = shakespeare[keyword]
    #search through list for appropriate sentance to print

