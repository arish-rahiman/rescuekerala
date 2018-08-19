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

class InventoryItemCategory(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=50)
    category = models.ForeignKey('InventoryItemCategory', on_delete=models.CASCADE)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Inventory Item"
        verbose_name_plural = "Inventory Items"

    def __str__(self):
        return self.name


class Volunteer(models.Model):
    USER_TYPE = CENTER_TYPE + (('AD', 'Admin'),)
    phone_number = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    user_type = models.CharField(max_length=2, choices=USER_TYPE)
    center = models.ForeignKey('Center', null=True, blank=True, on_delete=models.CASCADE)
    notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
    updated_at = models.DateTimeField(auto_now=True)
    update_log = models.TextField(null=True, blank=True)
    center_type = models.CharField(max_length=2, choices=CENTER_TYPE)
    district_center = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Center"
        verbose_name_plural = "Centers"


class ShipmentRequest(models.Model):
    STATUS = (
        ('RC', 'Request Created'),
        ('PC', 'Partially Completed'),
        ('CO', 'Completed'),
        ('DE', 'Delivered'),
    )

    delivery_to = models.ForeignKey('Center', on_delete=models.CASCADE)
    raised_by = models.ForeignKey('Volunteer', on_delete=models.CASCADE, related_name="+")
    status = models.CharField(max_length=3, choices=STATUS, default='RC')
    completed_at = models.DateTimeField(null=True, blank=True)
    completed_by = models.ForeignKey('Volunteer', null=True, blank=True, on_delete=models.CASCADE, related_name="+")
    notes = models.TextField(null=True, blank=True)
    is_urgent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Shipment Request"
        verbose_name_plural = "Shipment Requests"

REQUEST_ITEM_STATUS = (
    ('RC', 'Request Created'),
    ('PC', 'Partially Completed'),
    ('CO', 'Completed'),
    ('DE', 'Delivered'),
)


class ShipmentRequestItem(models.Model):
    shipment_request = models.ForeignKey('ShipmentRequest', on_delete=models.CASCADE)
    inventory_item = models.ForeignKey('InventoryItem', null=True, blank=True, on_delete=models.CASCADE)
    line_item = models.TextField(null=True, blank=True)
    qty = models.IntegerField()
    status = models.CharField(max_length=3, choices=REQUEST_ITEM_STATUS, default='RC')
    is_urgent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Shipment Request Item"
        verbose_name_plural = "Shipment Request Items"


class ShipmentRequestItemLog(models.Model):
    shipment_request_item = models.ForeignKey('ShipmentRequestItem', on_delete=models.CASCADE)
    responded_by = models.ForeignKey('Volunteer', on_delete=models.CASCADE)
    comment = models.TextField(null=True, blank=True)
    qty_promised = models.IntegerField()
    status_changed_to = models.CharField(max_length=3, choices=REQUEST_ITEM_STATUS, default='RC')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Shipment Request Item Log"
        verbose_name_plural = "Shipment Request Item Logs"


class InventoryItemStock(models.Model):
    item = models.ForeignKey('InventoryItem', on_delete=models.CASCADE)
    center = models.ForeignKey('Center', on_delete=models.CASCADE)
    updated_by = models.ForeignKey('Volunteer', on_delete=models.CASCADE)
    qty_available = models.IntegerField()
    qty_needed = models.IntegerField()
    admin_notes = models.TextField(null=True, blank=True)
    public_notes = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Inventory Item Stock"
        verbose_name_plural = "Inventory Item Stocks"


class InventoryItemStockLog(models.Model):
    inventory_item_stock = models.ForeignKey('InventoryItemStock', on_delete=models.CASCADE)
    updated_by = models.ForeignKey('Volunteer', on_delete=models.CASCADE)
    qty_available = models.IntegerField()
    qty_needed = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Inventory Item Stock Log"
        verbose_name_plural = "Inventory Item Stock Logs"
