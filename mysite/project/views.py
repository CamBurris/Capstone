from django.shortcuts import render, get_object_or_404, render_to_response
from project.models import Project
from project.forms import ProjectForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
	#latest_project_list = Project.objects.order_by('-id')[:5]
	#return render(request, 'project/index.html', {'latest_project_list': latest_project_list})
	project_list = Project.objects.all()
	paginator = Paginator(project_list, 5)
	page = request.GET.get('page')
	
	try:
		projects = paginator.page(page)
	except PageNotAnInteger:
		projects = paginator.page(1)
	except EmptyPage:
		projects = paginator.page(paginator.num_pages)
		
	return render(request, 'project/index.html', {'latest_project_list' : projects})
	
def detail(request, project_id):
	project = get_object_or_404(Project, pk=project_id)
	return render(request, 'project/detail.html', {'project':project})
	
def create(request):
	if request.POST:
		form = ProjectForm(request.POST)
		
		if form.is_valid():
			form.save()
			
			return HttpResponseRedirect('/project')
	else:
		form = ProjectForm()
		
	args = {}
	args.update(csrf(request))
	
	args['form'] = form
	
	return render_to_response('project/add.html', args)