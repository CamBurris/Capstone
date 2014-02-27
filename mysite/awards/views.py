from django.shortcuts import render
from awards.models import Award

# Create your views here.
def index(request):
	award_list = Award.objects.all
	return render(request, 'awards/index.html', {'award_list' : award_list})