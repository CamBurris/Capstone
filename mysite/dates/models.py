from django.db import models

# Create your models here.
class Date(models.Model):
	date = models.DateTimeField('Date')
	active = models.BooleanField(default=True)
	content = models.TextField()
	
	def __unicode__(self):
		return self.content