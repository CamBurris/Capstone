from django.db import models

# Create your models here.
class Project(models.Model):
	project_name = models.CharField(max_length=200)
	teacher_name = models.CharField(max_length=200)
	subject = models.CharField(max_length=200)
	phone = models.CharField(max_length=12)
	outlet = models.BooleanField()
	abstract = models.TextField()
	
	def __unicode__(self):
		return self.project_name
		
class Student(models.Model):
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
	grade = models.IntegerField()
	school = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=200)
	state = models.CharField(max_length=2)
	zip = models.IntegerField()
	phone = models.CharField(max_length=12)
	project = models.ForeignKey('Project')
	
	def __unicode__(self):
		return self.first_name
	