from django.shortcuts import render
from fset.forms import AuthorForm, BookFormset
from fset.models import Author, Book
from django.http import HttpResponseRedirect
from django.views.generic import CreateView

# Create your views here.
class index(CreateView):
	template_name = 'fset/form.html'
	model = Author
	form_class = AuthorForm
	success_url = 'fset/done.html'
	
	def get(self, request, *args, **kwargs):
		self.object = None
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		book_form = BookFormset()
		return self.render_to_response(
			self.get_context_data(form=form, book_form=book_form))
			
	def post(self, request, *args, **kwargs):
		self.object = None
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		book_form = BookFormset(self.request.POST)
		if(form.is_valid() and book_form.is_valid()):
			return self.form_valid(request, form, book_form)
		else:
			return self.form_invalid(form, book_form)
			
	def form_valid(self, request, form, book_form):
		self.object = form.save()
		book_form.instance = self.object
		book_form.save()
		
		return render(request, 'fset/done.html', {'abstract': self.object.name})
		#return HttpResponseRedirect(self.get_success_url())
		
	def form_invalid(self, form, book_form):
		return self.render_to_response(
			self.get_context_data(form=form, book_form=book_form))
'''def index(request):
	form = AuthorForm()
	bookformset = BookFormset(instance=Author(), prefix="books")
	
	if request.POST:
		form = AuthorForm(request.POST)
		
		if form.is_valid():
			author = form.save()
			
			bookformset = BookFormset(request.POST, instance=author)
			render(request, 'fset/done.html', {'form': form, 'bookformset': bookformset});
			
			if bookformset.is_valid():
				bookformset.save()
				return HttpResponseRedirect('/')
				
	return render(request, 'fset/form.html', {
		'form' : form,
		'bookformset' : bookformset,
		'action' : 'Create'})'''