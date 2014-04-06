from django.db import models

# Create your models here.
class Award(models.Model):
	awards = models.CharField(max_length=200)
	content = models.TextField()

	def __unicode__(self):
		return self.content