from django.db import models

# Create your models here.
class Link(models.Model):
	link = models.URLField(max_length=100)
	display = models.CharField(max_length=200)
	description = models.TextField()
	active = models.BooleanField(default=True)
	
	def __unicode__(self):
		return self.display