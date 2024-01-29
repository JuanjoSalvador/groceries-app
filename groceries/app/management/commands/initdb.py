import pandas as pd

from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError

from groceries.app.models import Product, Store


class Command(BaseCommand):
    help = "Initialize database"

    def add_arguments(self, parser):
        parser.add_argument("email", type=str)

    def handle(self, *args, **options):
        sample_data = "/workspaces/groceries-app/data/sample-data.ods"
        df_products = pd.read_excel(sample_data, engine='odf', sheet_name="products")
        df_stores = pd.read_excel(sample_data, engine='odf', sheet_name="stores")
        
        email = options['email']
        username = email.split("@")[0]

        for index, row in df_stores.iterrows():
            Store.objects.create(**row)

        for index, row in df_products.iterrows():
            product = {
                **row,
                "store": Store.objects.get(name=row['store'])
            }
            Product.objects.create(**product)

        call_command("createsuperuser", username=username, email=email)