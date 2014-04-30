from django.shortcuts import render
from studentProjects.models import ExtraForm

# Create your views here.
def index(request):
	return render(request, 'mysite/index.html', {})
	
def about(request):
	return render(request, 'about.html', {})
	
def forms(request):
	mandatoryForms = ExtraForm.objects.filter(required=True)
	otherForms = ExtraForm.objects.filter(required=False)
	return render(request, 'forms.html',{
		'mandatoryForms': mandatoryForms,
		'otherForms': otherForms})