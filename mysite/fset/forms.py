from django.forms.models import inlineformset_factory
from fset.models import Author, Book
from django import forms

class AuthorForm(forms.ModelForm):
	class Meta:
		model = Author
		
BookFormset = inlineformset_factory(Author, Book,
	fields = ('title',), can_delete=True)