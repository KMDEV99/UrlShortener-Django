from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from .forms import SubmitUrlForm
from .models import ShortenerURL

def home_view_fbv(reques, *args, **kwargs):
	return render(request, "shortener/home.html", {})

class HomeView(View):
	def get(self, request, *args, **kwargs):
		form = SubmitUrlForm()
		context = {
			"title": "Submit URL",
			"form": form
		}
		return render(request, "shortener/home.html", context)

	def post(self, request, *args, **kwargs):
		form = SubmitUrlForm(request.POST)
		context = {
			"title": "Submit URL",
			"form": form
		}
		template = "shortener/home.html"
		if form.is_valid():
			new_url = form.cleaned_data.get('url')
			obj, created = ShortenerURL.objects.get_or_create(url=new_url)
			context = {
				"object": obj,
				"form": form,
			}
			print(obj, "Has been added" if created else "")
			if created:
				template = "shortener/success.html"
			else:
				template = "shortener/already-exists.html"
		
		return render(request, template, context)

class ShortenerCBView(View):
	def get(self, request, short_url=None, *args, **kwargs):
		obj_url = None
		qs = ShortenerURL.objects.filter(short_url__iexact=short_url.upper())
		if qs.exists and qs.count() == 1:
			obj = qs.first()
			obj_url = obj.url
		return HttpResponse("hello {short_url}".format(short_url=obj_url))