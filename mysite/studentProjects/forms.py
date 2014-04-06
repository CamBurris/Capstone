from django import forms
from django.forms.models import inlineformset_factory
from studentProjects.models import Project, Student

class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		
StudentFormset = inlineformset_factory(Project, Student,
	fields= ('first_name', 'last_name', 'grade', 'school',
		'address', 'city', 'state', 'zip', 'phone',), can_delete=True)