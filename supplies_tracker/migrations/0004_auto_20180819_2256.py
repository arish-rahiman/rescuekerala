# Generated by Django 2.1 on 2018-08-19 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplies_tracker', '0003_inventoryitemstock_inventoryitemstocklog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventoryitemstock',
            options={'verbose_name': 'InventoryItemStock', 'verbose_name_plural': 'InventoryItemStocks'},
        ),
        migrations.AlterField(
            model_name='inventoryitemstock',
            name='qty_available',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='shipmentrequestitem',
            name='shipment_request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplies_tracker.ShipmentRequest'),
        ),
    ]
