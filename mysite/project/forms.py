from django import forms
from project.models import Project
#from taggit.forms import TagField

class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ['project_name', 'teacher_name', 'subject', 'outlet', 'abstract']
	
	#tags = TagField()