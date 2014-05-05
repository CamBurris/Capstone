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

s = set(stopwords.words('english'))
st = LancasterStemmer()

'''
Loads training data
'''
texts = []
files = os.listdir('AnimalSciences')
for file in files:
	f = open('./AnimalSciences/' + file, 'r')
	a = f.read()
	a = a.lower()
	a = re.findall(r'\w+', a, flags = re.UNICODE | re.LOCALE)
	a = [w for w in a if not w in s]
	for x in xrange(len(a)):
		a[x] = st.stem(a[x])
	texts.append((a, 'animal_science'))
	f.close()
	
files = os.listdir('BehavioralAndSocialSciences')
for file in files:
	f = open('./BehavioralAndSocialSciences/' + file, 'r')
	a = f.read()
	a = a.lower()
	a = re.findall(r'\w+', a, flags = re.UNICODE | re.LOCALE)
	a = [w for w in a if not w in s]
	for x in xrange(len(a)):
		a[x] = st.stem(a[x])
	texts.append((a, 'behavioral_science'))
	f.close()
	
files = os.listdir('Biochemistry')
for file in files:
	f = open('./Biochemistry/' + file, 'r')
	a = f.read()
	a = a.lower()
	a = re.findall(r'\w+', a, flags = re.UNICODE | re.LOCALE)
	a = [w for w in a if not w in s]
	for x in xrange(len(a)):
		a[x] = st.stem(a[x])
	texts.append((a, 'biochemistry'))
	f.close()
	
files = os.listdir('CellularAndMolecularBiology')
for file in files:
	f = open('./CellularAndMolecularBiology/' + file, 'r')
	a = f.read()
	a = a.lower()
	a = re.findall(r'\w+', a, flags = re.UNICODE | re.LOCALE)
	a = [w for w in a if not w in s]
	for x in xrange(len(a)):
		a[x] = st.stem(a[x])
	texts.append((a, 'cellular_biology'))
	f.close()
	
files = os.listdir('Chemistry')
for file in files:
	f = open('./Chemistry/' + file, 'r')
	a = f.read()
	a = a.lower()
	a = re.findall(r'\w+', a, flags = re.UNICODE | re.LOCALE)
	a = [w for w in a if not w in s]
	for x in xrange(len(a)):
		a[x] = st.stem(a[x])
	texts.append((a, 'chemistry'))
	f.close()
	
files = os.listdir('ComputerScience')
for file in files:
	f = open('./ComputerScience/' + file, 'r')
	a = f.read()
	a = a.lower()
	a = re.findall(r'\w+', a, flags = re.UNICODE | re.LOCALE)
	a = [w for w in a if not w in s]
	for x in xrange(len(a)):
		a[x] = st.stem(a[x])
	texts.append((a, 'computer_science'))
	f.close()
	
files = os.listdir('EarthAndPlanetaryScience')
for file in files:
	f = open('./EarthAndPlanetaryScience/' + file, 'r')
	a = f.read()
	a = a.lower()
	a = re.findall(r'\w+', a, flags = re.UNICODE | re.LOCALE)
	a = [w for w in a if not w in s]
	for x in xrange(len(a)):
		a[x] = st.stem(a[x])
	texts.append((a, 'earth_science'))
	f.close()
	
files = os.listdir('EngineeringElectricalMechanical')
for file in files:
	f = open('./EngineeringElectricalMechanical/' + file, 'r')
	a = f.read()
	a = a.lower()
	a = re.findall(r'\w+', a, flags = re.UNICODE | re.LOCALE)
	a = [w for w in a if not w in s]
	for x in xrange(len(a)):
		a[x] = st.stem(a[x])
	texts.append((a, 'engineering'))
	f.close()
	
files = os.listdir('EngineeringMaterialsBioengineering')
for file in files:
	f = open('./EngineeringMaterialsBioengineering/' + file, 'r')
	a = f.read()
	a = a.lower()
	a = re.findall(r'\w+', a, flags = re.UNICODE | re.LOCALE)
	a = [w for w in a if not w in s]
	for x in xrange(len(a)):
		a[x] = st.stem(a[x])
	texts.append((a, 'bioengineering'))
	f.close()
	
files = os.listdir('MathematicalSciences')
for file in files:
	f = open('./MathematicalSciences/' + file, 'r')
	a = f.read()
	a = a.lower()
	a = re.findall(r'\w+', a, flags = re.UNICODE | re.LOCALE)
	a = [w for w in a if not w in s]
	for x in xrange(len(a)):
		a[x] = st.stem(a[x])
	texts.append((a, 'math'))
	f.close()
	
files = os.listdir('MedicineAndHealthSciences')
for file in files:
	f = open('./MedicineAndHealthSciences/' + file, 'r')
	a = f.read()
	a = a.lower()
	a = re.findall(r'\w+', a, flags = re.UNICODE | re.LOCALE)
	a = [w for w in a if not w in s]
	for x in xrange(len(a)):
		a[x] = st.stem(a[x])
	texts.append((a, 'medicine'))
	f.close()
	
files = os.listdir('Microbiology')
for file in files:
	f = open('./Microbiology/' + file, 'r')
	a = f.read()
	a = a.lower()
	a = re.findall(r'\w+', a, flags = re.UNICODE | re.LOCALE)
	a = [w for w in a if not w in s]
	for x in xrange(len(a)):
		a[x] = st.stem(a[x])
	texts.append((a, 'microbiology'))
	f.close()
	
files = os.listdir('PhysicsAndAstronomy')
for file in files:
	f = open('./PhysicsAndAstronomy/' + file, 'r')
	a = f.read()
	a = a.lower()
	a = re.findall(r'\w+', a, flags = re.UNICODE | re.LOCALE)
	a = [w for w in a if not w in s]
	for x in xrange(len(a)):
		a[x] = st.stem(a[x])
	texts.append((a, 'physics'))
	f.close()
	
files = os.listdir('PlantSciences')
for file in files:
	f = open('./PlantSciences/' + file, 'r')
	a = f.read()
	a = a.lower()
	a = re.findall(r'\w+', a, flags = re.UNICODE | re.LOCALE)
	a = [w for w in a if not w in s]
	for x in xrange(len(a)):
		a[x] = st.stem(a[x])
	texts.append((a, 'plant_science'))
	f.close()

'''
Gets the features of an abstract

Returns boolean values indicating the presence of certain keywords

Also returns the eight most frequent words found in the abstract
'''	
def features(word_list):
	freq = FreqDist(word_list)
	f = freq.keys()
	return {
		'biology': 'biolog' in word_list,
		'engineering': 'engin' in word_list,
		'animal' : 'anim' in word_list,
		'behavior': 'behavy' in word_list,
		'chemistry': 'chem' in word_list,
		'health': 'heal' in word_list,
		'physics': 'phys' in word_list,
		'math': 'math' in word_list,
		'plant': 'plant' in word_list,
		'earth': 'earth' in word_list,
		'biochemistry': 'biochem' in word_list,
		'social': 'soc' in word_list,
		'planet': 'planet' in word_list,
		'temperature': 'temperature' in word_list,
		'blood': 'blood' in word_list,
		'tube': 'tube' in word_list,
		'pyschology': 'pyscholog' in word_list,
		'protein': 'protein' in word_list,
		'gene': 'gen' in word_list,
		'most_0': f[0],
		'most_1': f[1],
		'most_2': f[2],
		'most_3': f[3],
		'most_4': f[4],
		'most_5': f[5],
		'most_6': f[6],
		'most_7': f[7],
		}
		

#random.shuffle(texts)

#Get the feature sets of the training data
featuresets = [(features(text), label) for (text, label) in texts]
train_set = []
test_set = []

#Fill in train_set and test_set from training data
for x in xrange(len(featuresets)):
	if x % 2 == 0:
		train_set.append(featuresets[x])
	else:
		test_set.append(featuresets[x])	
		
#Create the classifier
classifier = NaiveBayesClassifier.train(train_set)
#print accuracy(classifier, test_set)
#classifier.show_most_informative_features(20)
f = open('abs1.txt', 'r')
a = f.read()
a = a.lower()
a = re.findall(r'\w+', a, flags = re.UNICODE | re.LOCALE)
a = [w for w in a if not w in s]
for x in xrange(len(a)):
	a[x] = st.stem(a[x])
print classifier.classify(features(a))