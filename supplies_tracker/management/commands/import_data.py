import csv
import os
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from supplies_tracker.models import InventoryItemCategory, InventoryItem, InventoryUnit

csv_path = os.path.abspath(os.path.dirname(__file__))

class Command(BaseCommand):

    def handle(self, *args, **options):
        self.create_category()

    def create_category(self):
        data = {}
        category_label = 'Category '
        sub_category_label = 'Sub-Category 1'
        item_label = 'Sub-Category 2'
        category = None
        sub_category = None
        with open(csv_path + '/item.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row[category_label] != "":
                    category = row[category_label]
                if row[sub_category_label] != "":
                    sub_category = row[sub_category_label]
                
                if item_label in row and row[item_label] != "":
                    if category and sub_category:
                        if category not in data:
                            data[category] = {}
                        if sub_category not in  data[category]:
                            data[category][sub_category] = []

                        data[category][sub_category].append({
                            "item": row[item_label],
                            "unit": row['Unit']
                        })
        for category, sub_categories in data.items():
            category, created = InventoryItemCategory.objects.update_or_create(name=category, defaults={
                'name':category
            })
            for sub_category, items in sub_categories.items():
                sub_category, created = InventoryItemCategory.objects.update_or_create(name=sub_category, parent=category, defaults={
                    'name':sub_category,
                    'parent':category
                })
                for item in items:
                    unit, create = InventoryUnit.objects.update_or_create(name=item['unit'], defaults={
                        'name':item['unit']
                    })
                    item, created = InventoryItem.objects.update_or_create(name=item['item'], category=sub_category, defaults={
                        'name':item['item'],
                        'unit':unit,
                        'category': sub_category
                    })
