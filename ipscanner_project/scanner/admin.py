from django.contrib import admin
from .models import ScanResult

# Register your models here.
@admin.register(ScanResult)
class ScanResultAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'scan_date')
    readonly_fields = ('scan_date',)