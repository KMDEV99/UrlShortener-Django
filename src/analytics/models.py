from django.db import models

from shortener_app.models import ShortenerURL


class ClickEventManager(models.Manager):
    def create_event(self, shortener_instance):
        if isinstance(shortener_instance, ShortenerURL):
            obj, created = self.get_or_create(shortener_url=shortener_instance)
            obj.count += 1
            obj.save()
            return obj.count
        return None

class ClickEvent(models.Model):
    shortener_url   = models.OneToOneField(ShortenerURL, on_delete=models.CASCADE)
    count       = models.IntegerField(default=0)
    create_date   = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return "{i}".format(i=self.count)