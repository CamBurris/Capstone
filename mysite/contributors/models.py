from django.db import models

# Create your models here.
class Contributor(models.Model):
	contributor = models.CharField(max_length = 200)
	
	def __unicode__(self):
		return self.contributor
