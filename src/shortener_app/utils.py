from string import ascii_lowercase, digits
from random import choice

from django.conf import settings

URL_LEN_MIN = getattr(settings, "URL_LEN_MIN", 6)

def url_generator(size=URL_LEN_MIN, chars=ascii_lowercase + digits):
	return ''.join(choice(chars) for _ in range(size))


def create_short_url(instance, size=URL_LEN_MIN):
	new_url = url_generator(size=size)
	klass = instance.__class__
	qs_exists = klass.objects.filter(short_url=new_url).exists()
	if qs_exists:
		return create_short_url(size=size)
	return new_url
