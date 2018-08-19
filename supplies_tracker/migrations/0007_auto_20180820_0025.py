# Generated by Django 2.1 on 2018-08-19 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplies_tracker', '0006_auto_20180819_2346'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryItemCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='supplies_tracker.InventoryItemCategory')),
            ],
        ),
        migrations.RemoveField(
            model_name='inventoryitem',
            name='name_ml',
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplies_tracker.InventoryItemCategory'),
        ),
    ]
