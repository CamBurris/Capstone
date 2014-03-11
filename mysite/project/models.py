from django.db import models
#from taggit.managers import TaggableManager

# Create your models here.
class Project(models.Model):
	BIOLOGY = 'BI'
	COMPSCI = 'CS'
	MATH = 'MH'
	subject_choices = (
		(BIOLOGY, 'Biology'),
		(COMPSCI, 'Computer Science'),
		(MATH, 'Mathmatetics'),
	)
	project_name = models.CharField(max_length=200)
	teacher_name = models.CharField(max_length=200)
	#subject = models.CharField(max_length=200)
	subject = models.CharField(max_length=2,
		choices=subject_choices,
		default=BIOLOGY)
	phone = models.CharField(max_length=12)
	outlet = models.BooleanField()
	abstract = models.TextField()
	#tags = TaggableManager()
	
	def __unicode__(self):
		return self.project_name