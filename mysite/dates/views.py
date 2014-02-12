from django.shortcuts import render
from dates.models import Date

# Create your views here.
def index(request):
	date_list = Date.objects.filter(active=True).order_by('date')
	return render(request, 'dates/index.html', {'date_list' : date_list})