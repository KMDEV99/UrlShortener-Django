from django.core.management.base import BaseCommand, CommandError

from shortener_app.models import ShortenerURL

class Command(BaseCommand):
    help = 'Prints list most recent 5 pairs (URL, Shortened URL) objects, prints all pairs with additional -a argument'

    def add_arguments(self, parser):
        parser.add_argument('-a', action='store_true', help='Print all pairs')

    def handle(self, *args, **options):
        return ShortenerURL.objects.print_urls(print_all=options['a'])