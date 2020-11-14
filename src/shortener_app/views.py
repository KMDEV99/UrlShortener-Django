from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.
def shortener_redirect_view(request, *args, **kwargs):
	return HttpResponse("hello")

class ShortenerCBView(View):
	def get(self, request, *args, **kwargs):
		return HttpResponse("Hello again")