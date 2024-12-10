from django.contrib import admin
from .models import ScanResult, ScanActivity



@admin.register(ScanResult)
class ScanResultAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'scan_date', 'status', 'scan_type', 'user', 'display_ports')  # Summary columns
    list_filter = ('status', 'scan_type', 'scan_date')  # Filters in the admin panel
    search_fields = ('ip_address', 'user__username', 'result')  # Searchable fields
    readonly_fields = ('scan_date', 'scan_duration', 'user')  # Read-only fields
    ordering = ['-scan_date']  # Default ordering by most recent scans

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

    def display_ports(self, obj):
        """
        Display open ports and their services in a readable format.
        """
        if obj.ports:
            return ", ".join([f"Port {p['port']} ({p.get('service', 'Unknown')})" for p in obj.ports])
        return "No open ports"

    display_ports.short_description = "Open Ports"

    def save_model(self, request, obj, form, change):
        """
        Custom save logic for ScanResult model.
        Automatically associate the logged-in user with the scan result if not already set.
        """
        if not obj.user:
            obj.user = request.user
        super().save_model(request, obj, form, change)


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

    def save_model(self, request, obj, form, change):
        """
        Custom save logic for ScanActivity model.
        Ensure ScanActivity is linked to the appropriate scan result.
        """
        if not obj.scan_result:
            obj.scan_result = ScanResult.objects.last()  # Associate with the latest scan if not set
        super().save_model(request, obj, form, change)
