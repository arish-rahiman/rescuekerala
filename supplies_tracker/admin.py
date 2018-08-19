from django.contrib import admin

from .models import InventoryItem, Volunteer, Center, InventoryItemStock


class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')


class VolunteerAdmin(BaseAdmin):
    list_filter = ('center', 'created_at', 'updated_at')
    list_display = ('get_name', 'phone_number')

    def get_name(self, obj):
        return obj.user.get_full_name()


class CenterAdmin(BaseAdmin):
    list_filter = ('district', 'status', 'center_type', 'created_at', 'updated_at')
    list_display = ('name', 'district')


class InventoryItemAdmin(BaseAdmin):
    list_filter = ('unit', 'category', 'created_at', 'updated_at')
    list_display = ('name', 'unit', 'category')


class InventoryItemStockAdmin(BaseAdmin):
    list_filter = ('item', 'center', 'created_at', 'updated_at')
    list_display = ('item', 'center', 'qty_available', 'qty_needed')


admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Center, CenterAdmin)
admin.site.register(InventoryItem, InventoryItemAdmin)
admin.site.register(InventoryItemStock, InventoryItemStockAdmin)
