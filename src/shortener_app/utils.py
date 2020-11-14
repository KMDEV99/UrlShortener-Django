from string import ascii_lowercase, digits
from random import choice


def url_generator(size=6, chars=ascii_lowercase + digits):
	return ''.join(choice(chars) for _ in range(size))


def create_short_url(instance, size=6):
	new_url = url_generator(size=size)
	klass = instance.__class__
	qs_exists = klass.objects.filter(short_url=new_url).exists()
	if qs_exists:
		return create_short_url(size=size)
	return new_url
	