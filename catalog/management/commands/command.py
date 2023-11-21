from django.core.management import BaseCommand
from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):

        Category.objects.all().delete()

        category_list = [
            {'name': 'телевизоры', 'description': 'большие'},
            {'name': 'телефоны', 'description': 'маленькие'}
        ]

        for category in category_list:
            Category.objects.create(**category)
