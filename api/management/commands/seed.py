from django.core.management.base import BaseCommand
import json
from api.models import Provider


class Command(BaseCommand):
    """Custom command to plant the seed """

    @staticmethod
    def plant_seed():
        """Load data and plant the seed."""
        with open('providers.json') as f:
            data = json.load(f)
            for item in data:
                Provider.create(item)

    def handle(self, *args, **kwargs):
        print("init plant seed")
        self.plant_seed()
        print("Seed has been planted")
