from django.shortcuts import render, render_to_response
from django.contrib.formtools.wizard.views import SessionWizardView
from studentProjects.models import Project, Student, ExtraForm
from studentProjects.forms import ProjectForm, StudentFormset
from django.views.generic import CreateView
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
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

inv = wn.synset('invertebrate.n.01')
vert = wn.synset('vertebrate.n.01')
person = [wn.synset('student.n.01'), 
	wn.synset('girl.n.01'), 
	wn.synset('boy.n.01'), 
	wn.synset('human.n.01'),
	wn.synset('man.n.01'),
	wn.synset('woman.n.01'),
	wn.synset('human.n.01'),
	wn.synset('child.n.02'),
	wn.synset('acquaintance.n.03')]
animal = wn.synset('animal.n.01')
pathogen = wn.synset('pathogen.n.01')
dna = wn.synset('deoxyribonucleic_acid.n.01')
s = set(stopwords.words('english'))

# Create your views here.
class index(CreateView):
	template_name = 'studentProjects/form.html'
	model = Project
	form_class = ProjectForm
	success_url = 'studentProjects/done.html'
	
	def get(self, request, *args, **kwargs):
		self.object = None
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		student_form = StudentFormset()
		return self.render_to_response(
			self.get_context_data(form=form, student_form=student_form))
			
	def post(self, request, *args, **kwargs):
		self.object = None
		valid = True
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		student_form = StudentFormset(self.request.POST)
		
		if(form.is_valid()):
			for sform in student_form:
				print 'in s loop'
				if(not sform.is_valid()):
					valid = False
		else:
			valid = False
			
		if(valid):
			return self.form_valid(request, form, student_form)
		else:
			return self.form_invalid(form, student_form)
			
	def form_valid(self, request, form, student_form):
		self.object = form.save()
		student_form.instance = self.object
		student_form.save()
		mandatoryForms = ExtraForm.objects.filter(required=True)
		optionalForms = ExtraForm.objects.filter(required=False)
		# nltk stuff goes here
		
		a = self.object.abstract
		a = a.lower()
		a = re.findall(r'\w+', a, flags = re.UNICODE | re.LOCALE)
		a = [w for w in a if not w in s]
		p = HasPerson(a)
		v = HasVertebrate(a)
		q = HasQualified(a)
		otherForms = []
		
		for form in optionalForms:
			if form.name == "Human Subjects and Informed Consent":
				otherForms.append((form, p))
			elif form.name == "Nonhuman Vertebrate Animal":
				otherForms.append((form, v))
			elif form.name == "Qualified Scientist":
				otherForms.append((form, q))
			else:
				otherForms.append((form, False))
		
		return render(request, 'studentProjects/done.html', {
			'project_name': self.object.project_name,
			'teacher_name': self.object.teacher_name,
			'subject': self.object.subject,
			'phone': self.object.phone,
			'outlet': self.object.outlet,
			'abstract': self.object.abstract,
			'mandatoryForms': mandatoryForms,
			'otherForms': otherForms})
		#return HttpResponseRedirect(self.get_success_url())
		
	def form_invalid(self, form, student_form):
		return self.render_to_response(
			self.get_context_data(form=form, student_form=student_form))