from nltk.classify import NaiveBayesClassifier
from nltk.tokenize import word_tokenize
#from nltk.book import *
from nltk import FreqDist
import os
from nltk.corpus import stopwords
import re
import random
from nltk.classify import accuracy
from nltk.stem.lancaster import LancasterStemmer
from nltk.corpus import wordnet as wn
from nltk.corpus.reader import NOUN

def HasQualified(word_list):
	for word in word_list:
		if HasAnimal(word_list) or HasPathogen(word_list) or HasDNA(word_list):
			return True
	
	return False
	
def HasAnimal(word_list):
	for word in word_list:
		if IsAnimal(word) and not IsPerson(word):
			print word
			return True
	
	return False
	
def IsAnimal(word):
	a = wn.synsets(word, NOUN)
	if a:
		d = a[0]
	else: 
		return False
		
	b = d.hypernym_distances()
	for h in b:
		if h[0] == animal:
			return True
			
	return False
	
def HasPathogen(word_list):
	for word in word_list:
		if IsPathogen(word):
			print word
			return True
	
	return False
	
def IsPathogen(word):
	a = wn.synsets(word, NOUN)
	if a:
		d = a[0]
	else:
		return False
		
	b = d.hypernym_distances()
	for h in b:
		if h[0] == pathogen:
			return True
			
	return False
	
def HasDNA(word_list):
	for word in word_list:
		if IsDNA(word):
			print word
			return True
	
	return False
	
def IsDNA(word):
	a = wn.synsets(word, NOUN)
	if a:
		d = a[0]
	else:
		return False
		
	b = d.hypernym_distances()
	for h in b:
		if h[0] == dna:
			return True
			
	return False

def HasPerson(word_list):
	for word in word_list:
		if IsPerson(word):
			print word
			return True
	
	return False
	
def IsPerson(word):
	a = wn.synsets(word, NOUN)
	if a:
		d = a[0]
	else:
		return False
		
	b = d.hypernym_distances()
	for h in b:
		if h[0] in person:
			return True
			
	return False

def HasVertebrate(word_list):
	for word in word_list:
		if IsVertebrate(word) and not IsPerson(word):
			print word
			return True
	
	return False

def IsVertebrate(word):
	a = wn.synsets(word, NOUN)
	if a:
		d = a[0]
	else: 
		return False
		
	b = d.hypernym_distances()
	for h in b:
		if h[0] == inv:
			return False
		elif h[0] == vert:
			return True
			
	return False

s = set(stopwords.words('english'))
st = LancasterStemmer()

inv = wn.synset('invertebrate.n.01')
vert = wn.synset('vertebrate.n.01')
person = [wn.synset('student.n.01'), 
	wn.synset('girl.n.01'), 
	wn.synset('boy.n.01'), 
	wn.synset('human.n.01'),
	wn.synset('man.n.01'),
	wn.synset('woman.n.01'),
	wn.synset('human.n.01')]
animal = wn.synset('animal.n.01')
pathogen = wn.synset('pathogen.n.01')
dna = wn.synset('deoxyribonucleic_acid.n.01')

f = open('test.txt', 'r')
a = f.read()
a.lower()
a = a.lower()
a = re.findall(r'\w+', a, flags = re.UNICODE | re.LOCALE)
a = [w for w in a if not w in s]

print HasPerson(a), HasVertebrate(a), HasQualified(a)