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
'''
This is a working file for interfacing with Wordnet

This code has been integrated with the Django application
'''

'''
This method returns a boolean indicating if a word list
has the features to qualify for the Qualifed Scientis form
'''
def HasQualified(word_list):
	for word in word_list:
		if HasAnimal(word_list) or HasPathogen(word_list) or HasDNA(word_list):
			return True
	
	return False
	
'''
This method returns a boolean indicating if a word list
has a nonhuman animal in it
'''
def HasAnimal(word_list):
	for word in word_list:
		if IsAnimal(word) and not IsPerson(word):
			print word
			return True
	
	return False

'''
This method returns if a single word is an animal or not
'''	
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

'''
This method returns a boolean indicating if a word list
has a pathogen or not
'''
def HasPathogen(word_list):
	for word in word_list:
		if IsPathogen(word):
			print word
			return True
	
	return False

'''
This method returns whether or not a word is a pathogen
'''	
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

'''
This method returns a boolean indicating if a word list
mentions DNA or parts of DNA
'''	
def HasDNA(word_list):
	for word in word_list:
		if IsDNA(word):
			print word
			return True
	
	return False

'''
This method returns a boolean indicating if a word is a
part of DNA or related to DNA
'''	
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

'''
This method returns a boolean indicating if a word list
mentions a person
'''
def HasPerson(word_list):
	for word in word_list:
		if IsPerson(word):
			print word
			return True
	
	return False

'''
This method returns wether or not a word is related to a person
'''	
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

'''
This method returns a boolean indicating if a word list
has a nonhuman vertebrate animal
'''
def HasVertebrate(word_list):
	for word in word_list:
		if IsVertebrate(word) and not IsPerson(word):
			print word
			return True
	
	return False

'''
This method returns wether or not a word is a nonhuman
vertebrate animal
'''
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

'''
Definitions for synsets

Used to determine is-a relationships
'''
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

'''
Loads abstract training data
'''
texts = []
files = os.listdir('AnimalSciences')
for file in files:
	f = open('./AnimalSciences/' + file, 'r')
	a = f.read()
	a = a.lower()
	a = re.findall(r'\w+', a, flags = re.UNICODE | re.LOCALE)
	a = [w for w in a if not w in s]
	texts.append((a, 'animal_science'))
	f.close()
	
files = os.listdir('BehavioralAndSocialSciences')
for file in files:
	f = open('./BehavioralAndSocialSciences/' + file, 'r')
	a = f.read()
	a = a.lower()
	a = re.findall(r'\w+', a, flags = re.UNICODE | re.LOCALE)
	a = [w for w in a if not w in s]

	texts.append((a, 'behavioral_science'))
	f.close()
	
files = os.listdir('Biochemistry')
for file in files:
	f = open('./Biochemistry/' + file, 'r')
	a = f.read()
	a = a.lower()
	a = re.findall(r'\w+', a, flags = re.UNICODE | re.LOCALE)
	a = [w for w in a if not w in s]

	texts.append((a, 'biochemistry'))
	f.close()
	
files = os.listdir('CellularAndMolecularBiology')
for file in files:
	f = open('./CellularAndMolecularBiology/' + file, 'r')
	a = f.read()
	a = a.lower()
	a = re.findall(r'\w+', a, flags = re.UNICODE | re.LOCALE)
	a = [w for w in a if not w in s]

	texts.append((a, 'cellular_biology'))
	f.close()
	
files = os.listdir('Chemistry')
for file in files:
	f = open('./Chemistry/' + file, 'r')
	a = f.read()
	a = a.lower()
	a = re.findall(r'\w+', a, flags = re.UNICODE | re.LOCALE)
	a = [w for w in a if not w in s]

	texts.append((a, 'chemistry'))
	f.close()
	
files = os.listdir('ComputerScience')
for file in files:
	f = open('./ComputerScience/' + file, 'r')
	a = f.read()
	a = a.lower()
	a = re.findall(r'\w+', a, flags = re.UNICODE | re.LOCALE)
	a = [w for w in a if not w in s]

	texts.append((a, 'computer_science'))
	f.close()
	
files = os.listdir('EarthAndPlanetaryScience')
for file in files:
	f = open('./EarthAndPlanetaryScience/' + file, 'r')
	a = f.read()
	a = a.lower()
	a = re.findall(r'\w+', a, flags = re.UNICODE | re.LOCALE)
	a = [w for w in a if not w in s]

	texts.append((a, 'earth_science'))
	f.close()
	
files = os.listdir('EngineeringElectricalMechanical')
for file in files:
	f = open('./EngineeringElectricalMechanical/' + file, 'r')
	a = f.read()
	a = a.lower()
	a = re.findall(r'\w+', a, flags = re.UNICODE | re.LOCALE)
	a = [w for w in a if not w in s]

	texts.append((a, 'engineering'))
	f.close()
	
files = os.listdir('EngineeringMaterialsBioengineering')
for file in files:
	f = open('./EngineeringMaterialsBioengineering/' + file, 'r')
	a = f.read()
	a = a.lower()
	a = re.findall(r'\w+', a, flags = re.UNICODE | re.LOCALE)
	a = [w for w in a if not w in s]

	texts.append((a, 'bioengineering'))
	f.close()
	
files = os.listdir('MathematicalSciences')
for file in files:
	f = open('./MathematicalSciences/' + file, 'r')
	a = f.read()
	a = a.lower()
	a = re.findall(r'\w+', a, flags = re.UNICODE | re.LOCALE)
	a = [w for w in a if not w in s]

	texts.append((a, 'math'))
	f.close()
	
files = os.listdir('MedicineAndHealthSciences')
for file in files:
	f = open('./MedicineAndHealthSciences/' + file, 'r')
	a = f.read()
	a = a.lower()
	a = re.findall(r'\w+', a, flags = re.UNICODE | re.LOCALE)
	a = [w for w in a if not w in s]

	texts.append((a, 'medicine'))
	f.close()
	
files = os.listdir('Microbiology')
for file in files:
	f = open('./Microbiology/' + file, 'r')
	a = f.read()
	a = a.lower()
	a = re.findall(r'\w+', a, flags = re.UNICODE | re.LOCALE)
	a = [w for w in a if not w in s]

	texts.append((a, 'microbiology'))
	f.close()
	
files = os.listdir('PhysicsAndAstronomy')
for file in files:
	f = open('./PhysicsAndAstronomy/' + file, 'r')
	a = f.read()
	a = a.lower()
	a = re.findall(r'\w+', a, flags = re.UNICODE | re.LOCALE)
	a = [w for w in a if not w in s]

	texts.append((a, 'physics'))
	f.close()
	
files = os.listdir('PlantSciences')
for file in files:
	f = open('./PlantSciences/' + file, 'r')
	a = f.read()
	a = a.lower()
	a = re.findall(r'\w+', a, flags = re.UNICODE | re.LOCALE)
	a = [w for w in a if not w in s]

	texts.append((a, 'plant_science'))
	f.close()

'''
Runs form recommendations on training data
'''	
for text in texts:
	print 'P:', HasPerson(text[0]), 'V:', HasVertebrate(text[0]), 'Q:', HasQualified(text[0])