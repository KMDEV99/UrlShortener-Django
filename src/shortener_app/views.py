from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from analytics.models import ClickEvent

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

class URL_Redirect(View):
	def get(self, request, short_url=None, *args, **kwargs):
		qs = ShortenerURL.objects.filter(short_url__iexact=short_url)
		if qs.count() != 1 and not qs.exists():
			raise Http404
		obj = qs.first()
		print(ClickEvent.objects.create_event(obj))
		return HttpResponseRedirect(obj.url)
