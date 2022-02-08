from django.core.management import BaseCommand

from authapp.models import User, UserProfile
from baskets.models import Basket
from mainapp.models import ProductCategory, Product


class Command(BaseCommand):
    def handle(self, *args, **options):

        Basket.objects.all().delete()
        UserProfile.objects.all().delete()
        User.objects.all().delete()
        Product.objects.all().delete()
        ProductCategory.objects.all().delete()