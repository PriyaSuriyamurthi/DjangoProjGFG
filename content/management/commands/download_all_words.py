from django.core.management.base import BaseCommand, CommandError
from content.utils import compute


class Command(BaseCommand):
    help = 'calls the API to fetch word'

    def handle(self, *args, **options):
        compute()
