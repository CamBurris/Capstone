from django.db import models

# Create your models here.
class Author(models.Model):
	name = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.name
		
class Book(models.Model):
	author = models.ForeignKey(Author)
	title = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.title