# Generated by Django 2.1 on 2018-08-19 19:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplies_tracker', '0008_merge_20180820_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryitem',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='center',
        ),
        migrations.AddField(
            model_name='volunteer',
            name='center',
            field=models.ManyToManyField(blank=True, null=True, to='supplies_tracker.Center'),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
