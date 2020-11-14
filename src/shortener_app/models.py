from django.db import models
from django.conf import settings

from .utils import url_generator, create_short_url
# Create your models here.


URL_LEN_MAX = getattr(settings, "URL_LEN_MAX", 15)


class ShortenerURLManager(models.Manager):
	def all(self, args, **kwargs):
		qs_main = super(ShortenerURLManager, self).all(*args, **kwargs)
		qs = qs_main.filter(active=True)
		return qs

	def print_urls(self, print_all=False):
		qs = ShortenerURL.objects.filter(id__gte=1) if print_all else ShortenerURL.objects.filter(id__gte=1)[:5]
		urls = [(url.url, url.short_url) for url in qs]
		return str(urls)

class ShortenerURL(models.Model):
	url = models.CharField(max_length=200)
	short_url = models.CharField(max_length=URL_LEN_MAX, unique=True, blank=True)
	create_date = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=True)

	objects = ShortenerURLManager()

	def save(self, *args, **kwargs):
		if not self.short_url:
			self.short_url = create_short_url(self)
		super(ShortenerURL, self).save(*args, **kwargs)

	def __str__(self):
		return str(self.url)

	def __unicode(self):
		return str(self.url)
