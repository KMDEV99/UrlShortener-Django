from django.db import models

# Create your models here.

class ShortenerURL(models.Model):
	url = models.CharField(max_length=200, )
	shortcode = models.CharField(max_length=20, unique=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return str(self.url)

	def __unicode(self):
		return str(self.url)
