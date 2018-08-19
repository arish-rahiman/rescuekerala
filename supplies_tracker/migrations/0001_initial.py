# Generated by Django 2.1 on 2018-08-19 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Center',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_id', models.CharField(max_length=100)),
                ('coordinator', models.CharField(blank=True, max_length=100, null=True)),
                ('district', models.CharField(choices=[('alp', 'Alappuzha - ആലപ്പുഴ'), ('ekm', 'Ernakulam - എറണാകുളം'), ('idk', 'Idukki - ഇടുക്കി'), ('knr', 'Kannur - കണ്ണൂർ'), ('ksr', 'Kasaragod - കാസർഗോഡ്'), ('kol', 'Kollam - കൊല്ലം'), ('ktm', 'Kottayam - കോട്ടയം'), ('koz', 'Kozhikode - കോഴിക്കോട്'), ('mpm', 'Malappuram - മലപ്പുറം'), ('pkd', 'Palakkad - പാലക്കാട്'), ('ptm', 'Pathanamthitta - പത്തനംതിട്ട'), ('tvm', 'Thiruvananthapuram - തിരുവനന്തപുരം'), ('tcr', 'Thrissur - തൃശ്ശൂർ'), ('wnd', 'Wayanad - വയനാട്')], max_length=3)),
                ('status', models.BooleanField(choices=[(True, 'Open'), (False, 'Closed')], default=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('public_notes', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('update_log', models.TextField(blank=True, null=True)),
                ('center_type', models.CharField(choices=[('DC', 'District Center'), ('RC', 'Rescue Center'), ('CC', 'Collection Center')], max_length=2)),
                ('name', models.CharField(max_length=100)),
                ('district_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplies_tracker.Center')),
            ],
            options={
                'verbose_name': 'Center',
                'verbose_name_plural': 'Centers',
            },
        ),
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('name_ml', models.CharField(max_length=100)),
                ('unit', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('FD', 'Food'), ('ME', 'Medicine'), ('NF', 'Non-Food')], max_length=2)),
                ('notes', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'InventoryItem',
                'verbose_name_plural': 'InventoryItems',
            },
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=100)),
                ('user_type', models.CharField(choices=[('DC', 'District Center'), ('RC', 'Rescue Center'), ('CC', 'Collection Center'), ('AD', 'Admin')], max_length=2)),
                ('notes', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('center', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='supplies_tracker.Center')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Volunteer',
                'verbose_name_plural': 'Volunteers',
            },
        ),
    ]
