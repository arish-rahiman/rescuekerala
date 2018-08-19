from django.contrib.auth.models import User
from django.db import models

# Create your models here.
DISTRICTS = (
    ('alp', 'Alappuzha - ആലപ്പുഴ'),
    ('ekm', 'Ernakulam - എറണാകുളം'),
    ('idk', 'Idukki - ഇടുക്കി'),
    ('knr', 'Kannur - കണ്ണൂർ'),
    ('ksr', 'Kasaragod - കാസർഗോഡ്'),
    ('kol', 'Kollam - കൊല്ലം'),
    ('ktm', 'Kottayam - കോട്ടയം'),
    ('koz', 'Kozhikode - കോഴിക്കോട്'),
    ('mpm', 'Malappuram - മലപ്പുറം'),
    ('pkd', 'Palakkad - പാലക്കാട്'),
    ('ptm', 'Pathanamthitta - പത്തനംതിട്ട'),
    ('tvm', 'Thiruvananthapuram - തിരുവനന്തപുരം'),
    ('tcr', 'Thrissur - തൃശ്ശൂർ'),
    ('wnd', 'Wayanad - വയനാട്'),
)

CENTER_TYPE = (
    ('DC', 'District Center'),
    ('RC', 'Rescue Center'),
    ('CC', 'Collection Center'),
)


class InventoryItem(models.Model):
    ITEM_TYPE = (
        ('FD', 'Food'),
        ('ME', 'Medicine'),
        ('NF', 'Non-Food'),
    )
    name = models.CharField(max_length=100)
    name_ml = models.CharField(max_length=100)
    unit = models.CharField(max_length=50)
    category = models.CharField(max_length=2, choices=ITEM_TYPE)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "InventoryItem"
        verbose_name_plural = "InventoryItems"

    def __str__(self):
        return self.name


class Volunteer(models.Model):
    USER_TYPE = CENTER_TYPE + (('AD', 'Admin'),)
    phone_number = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=2, choices=USER_TYPE)
    center = models.ForeignKey('Center', null=True, blank=True, on_delete=models.CASCADE)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Volunteer"
        verbose_name_plural = "Volunteers"


class Center(models.Model):
    CENTER_STATUS = (
        (True, 'Open'),
        (False, 'Closed'),
    )
    name = models.CharField(max_length=100)
    serial_id = models.CharField(max_length=100)
    coordinator = models.CharField(max_length=100, null=True, blank=True)
    district = models.CharField(max_length=3, choices=DISTRICTS)
    status = models.BooleanField(default=True, choices=CENTER_STATUS)
    notes = models.TextField(null=True, blank=True)
    public_notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    update_log = models.TextField(null=True, blank=True)
    center_type = models.CharField(max_length=2, choices=CENTER_TYPE)
    name = models.CharField(max_length=100)
    district_center = models.ForeignKey('self', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Center"
        verbose_name_plural = "Centers"
