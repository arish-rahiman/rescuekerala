from django.contrib import admin

from .models import InventoryItem, Volunteer, Center, InventoryItemStock


class BaseAdmin(admin.ModelAdmin):
    exclude = ('created_at', 'updated_at')

class VolunteerAdmin(BaseAdmin):
    list_display = ('get_center', 'get_name', 'phone_number')

    def get_name(self, obj):
        return obj.user.get_full_name()

    def get_center(self, obj):
        return "\n".join([c.name for c in obj.center.all()])


class CenterAdmin(BaseAdmin):
    list_filter = ('district', 'status', 'center_type', 'notes')
    list_display = ('name', 'district')


class InventoryItemAdmin(BaseAdmin):
    list_filter = ('unit', 'category')
    list_display = ('name', 'unit', 'category')


admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Center, CenterAdmin)
admin.site.register(InventoryItem, InventoryItemAdmin)