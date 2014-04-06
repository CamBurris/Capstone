from django.shortcuts import render, render_to_response
from django.contrib.formtools.wizard.views import SessionWizardView
from studentProjects.models import Project, Student
from studentProjects.forms import ProjectForm, StudentFormset
from django.views.generic import CreateView

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
		
		# nltk stuff goes here
		
		return render(request, 'studentProjects/done.html', {'abstract': self.object.abstract})
		#return HttpResponseRedirect(self.get_success_url())
		
	def form_invalid(self, form, student_form):
		return self.render_to_response(
			self.get_context_data(form=form, student_form=student_form))