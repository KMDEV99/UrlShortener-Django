from django.contrib import admin
from django.urls import path, re_path

from shortener_app.views import URL_Redirect, HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', HomeView.as_view()),
    re_path(r'b/(?P<short_url>[\w-]{6,15})/$', URL_Redirect.as_view(), name='short_url'),
]
