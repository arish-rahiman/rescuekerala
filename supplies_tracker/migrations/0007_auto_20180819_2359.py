# Generated by Django 2.1 on 2018-08-19 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supplies_tracker', '0006_auto_20180819_2346'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventoryitem',
            options={'verbose_name': 'Inventory Item', 'verbose_name_plural': 'Inventory Items'},
        ),
        migrations.AlterModelOptions(
            name='inventoryitemstock',
            options={'verbose_name': 'Inventory Item Stock', 'verbose_name_plural': 'Inventory Item Stocks'},
        ),
        migrations.AlterModelOptions(
            name='inventoryitemstocklog',
            options={'verbose_name': 'Inventory Item Stock Log', 'verbose_name_plural': 'Inventory Item Stock Logs'},
        ),
        migrations.AlterModelOptions(
            name='shipmentrequest',
            options={'verbose_name': 'Shipment Request', 'verbose_name_plural': 'Shipment Requests'},
        ),
        migrations.AlterModelOptions(
            name='shipmentrequestitem',
            options={'verbose_name': 'Shipment Request Item', 'verbose_name_plural': 'Shipment Request Items'},
        ),
        migrations.AlterModelOptions(
            name='shipmentrequestitemlog',
            options={'verbose_name': 'Shipment Request Item Log', 'verbose_name_plural': 'Shipment Request Item Logs'},
        ),
    ]
