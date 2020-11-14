from django.db import models
from string import ascii_lowercase, digits
from random import choice
# Create your models here.

def url_generator(size=6, chars=ascii_lowercase + digits):
	return ''.join(choice(chars) for _ in range(size))

class ShortenerURL(models.Model):
	url = models.CharField(max_length=200, )
	short_url = models.CharField(max_length=20, unique=True)
	create_date = models.DateTimeField(auto_now_add=True)

	def save(self, *args, **kwargs):
		self.short_url = url_generator()
		super(ShortenerURL, self).save(*args, **kwargs)

	def __str__(self):
		return str(self.url)

	def __unicode(self):
		return str(self.url)
