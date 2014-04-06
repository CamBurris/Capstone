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