from django.contrib import admin
from .models import ScanResult, ScanActivity


@admin.register(ScanResult)
class ScanResultAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'scan_date', 'status', 'scan_type', 'user', 'display_ports')  # Summary columns
    list_filter = ('status', 'scan_type', 'scan_date')  # Filters in the admin panel
    search_fields = ('ip_address', 'user__username', 'result')  # Searchable fields
    readonly_fields = ('scan_date', 'scan_duration', 'user')  # Read-only fields
    fieldsets = (
        (None, {
            'fields': ('ip_address', 'status', 'scan_type', 'result')
        }),
        ('Advanced Details', {
            'fields': ('ports', 'services', 'operating_system', 'scan_duration')
        }),
        ('User Information', {
            'fields': ('user',)
        }),
    )
    ordering = ['-scan_date']  # Default ordering by most recent scans

    def display_ports(self, obj):
        """
        Display open ports and their services in a readable format.
        """
        if obj.ports:
            return ", ".join([f"Port {p['port']} ({p.get('service', 'Unknown')})" for p in obj.ports])
        return "No open ports"

    display_ports.short_description = "Open Ports"


@admin.register(ScanActivity)
class ScanActivityAdmin(admin.ModelAdmin):
    list_display = ('scan_result', 'timestamp', 'action', 'details')  # Display fields
    list_filter = ('timestamp', 'action')  # Filters
    search_fields = ('scan_result__ip_address', 'action', 'details')  # Searchable fields
    readonly_fields = ('timestamp',)  # Make timestamp read-only

    def get_scan_summary(self, obj):
        """
        Display a summary of the associated scan result.
        """
        return obj.scan_result.get_scan_summary()

    get_scan_summary.short_description = "Scan Summary"
