from django.shortcuts import render
from contributors.models import Contributor

# Create your views here.
def index(request):
	contributor_list = Contributor.objects.all
	return render(request, 'contributors/index.html' , {'contributor_list' : contributor_list})
