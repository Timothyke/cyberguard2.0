from django.contrib import admin
from .models import ScanResult

@admin.register(ScanResult)
class ScanResultAdmin(admin.ModelAdmin):
    # Displayed columns in the admin list view
    list_display = ('ip_address', 'scan_date', 'status', 'scan_type', 'operating_system', 'user')

    # Searchable fields in the admin
    search_fields = ('ip_address', 'status', 'operating_system', 'user__username')

    # Filter options in the sidebar
    list_filter = ('status', 'scan_type', 'scan_date', 'user')

    # Read-only fields to prevent accidental changes to critical info
    readonly_fields = ('ip_address', 'scan_date', 'result', 'scan_duration')

    # Fieldsets for grouping fields in the detail view
    fieldsets = (
        ('Scan Details', {
            'fields': ('ip_address', 'scan_date', 'status', 'scan_type', 'scan_duration', 'result')
        }),
        ('Additional Information', {
            'fields': ('operating_system', 'ports', 'services', 'user')
        }),
    )

    # Pagination for large datasets
    list_per_page = 25
