from django.db import models
from .utils import url_generator 
# Create your models here.


class ShortenerURL(models.Model):
	url = models.CharField(max_length=200, )
	short_url = models.CharField(max_length=20, unique=True)
	create_date = models.DateTimeField(auto_now_add=True)

	def save(self, *args, **kwargs):
		if not self.short_url:
			self.short_url = url_generator()
		super(ShortenerURL, self).save(*args, **kwargs)

	def __str__(self):
		return str(self.url)

	def __unicode(self):
		return str(self.url)
