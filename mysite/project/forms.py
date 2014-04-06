from django import forms
from project.models import Project

class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ['project_name', 'teacher_name', 'subject', 'outlet', 'abstract']