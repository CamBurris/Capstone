from django.shortcuts import render
from links.models import Link

# Create your views here.
def index(request):
	link_list = Link.objects.filter(active=True)
	return render(request, 'links/index.html', {'link_list' : link_list})