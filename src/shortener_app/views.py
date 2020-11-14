from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import ShortenerURL
# Create your views here.


def home_view_fbv(reques, *args, **kwargs):
	if request.method == 'POST':
		print(request.POST)
	return render(request, "shortener/home.html", {})

class HomeView(View):
	def get(self, request, *args, **kwargs):
		return render(request, "shortener/home.html", {})

	def post(self, request, *args, **kwargs):
		print(request.POST)
		print(request.POST.get('url'))
		return render(request, "shortener/home.html", {})

class ShortenerCBView(View):
	def get(self, request, short_url=None, *args, **kwargs):
		obj_url = None
		qs = ShortenerURL.objects.filter(short_url__iexact=short_url.upper())
		if qs.exists and qs.count() == 1:
			obj = qs.first()
			obj_url = obj.url
		return HttpResponse("hello {short_url}".format(short_url=obj_url))