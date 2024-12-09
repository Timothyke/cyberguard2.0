from django.db import models
from django.contrib.auth.models import User

class ScanResult(models.Model):
    # Basic fields
    ip_address = models.GenericIPAddressField(db_index=True)  # Indexed for faster lookups
    scan_date = models.DateTimeField(auto_now_add=True, db_index=True)  # Automatically set the date, indexed
    result = models.TextField()  # Store the raw output of the scan
    status = models.CharField(
        max_length=50,
        choices=[('success', 'Success'), ('failed', 'Failed')],
        default='success'
    )
    
    # Additional fields
    ports = models.JSONField(default=list)  # Open ports and their services (JSON format)
    scan_duration = models.DurationField(null=True, blank=True)  # Nullable scan duration
    scan_type = models.CharField(
        max_length=20,
        choices=[('fast', 'Fast Scan'), ('full', 'Full Scan')],
        default='fast'
    )
    operating_system = models.CharField(max_length=255, blank=True, null=True)  # OS detected during scan
    services = models.JSONField(default=dict)  # Services per open port (JSON format)

    # User who initiated the scan
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    # Methods
    def __str__(self) -> str:
        return f"Scan for {self.ip_address} on {self.scan_date.strftime('%Y-%m-%d %H:%M:%S')} - {self.status}"

    def display_ports(self) -> str:
        """
        Return a comma-separated string of open ports and their services in a readable format.
        """
        return ', '.join([f"Port {port.get('port')} ({port.get('service', 'Unknown')})" for port in self.ports])

    def get_scan_summary(self) -> str:
        """
        Provide a user-friendly summary of the scan result.
        """
        summary = f"Scan for {self.ip_address} performed on {self.scan_date.strftime('%Y-%m-%d %H:%M:%S')}. "
        summary += f"Status: {self.status}. Scan type: {self.scan_type}. "
        if self.status == 'success':
            summary += f"Open ports: {self.display_ports()}."
        else:
            summary += "Scan failed."
        return summary

    def get_scan_duration_in_seconds(self) -> float | None:
        """
        Get the scan duration in seconds if available.
        """
        if self.scan_duration:
            return self.scan_duration.total_seconds()
        return None

    def save_scan_data(self, ports: list[dict], services: dict, os_info: str = None) -> None:
        """
        Save parsed scan result data (ports, services, and OS information).
        """
        self.ports = ports
        self.services = services
        if os_info:
            self.operating_system = os_info
        self.save()

    # Class methods
    @classmethod
    def get_successful_scans(cls, user: User = None):
        """
        Retrieve all successful scans, optionally filtered by user.
        """
        queryset = cls.objects.filter(status='success')
        if user:
            queryset = queryset.filter(user=user)
        return queryset

    @classmethod
    def get_failed_scans(cls, user: User = None):
        """
        Retrieve all failed scans, optionally filtered by user.
        """
        queryset = cls.objects.filter(status='failed')
        if user:
            queryset = queryset.filter(user=user)
        return queryset

    # Meta options
    class Meta:
        ordering = ['-scan_date']  # Default ordering by most recent scans
        verbose_name = 'Scan Result'
        verbose_name_plural = 'Scan Results'

class ScanActivity(models.Model):
    """
    Model to log activities related to ScanResults.
    """
    scan_result = models.ForeignKey(ScanResult, on_delete=models.CASCADE, related_name='activities')
    timestamp = models.DateTimeField(auto_now_add=True)
    action = models.CharField(max_length=255)  # Example: "Started Scan", "Finished Scan", "Viewed Results"
    details = models.TextField(blank=True, null=True)  # Additional context for the action

    def __str__(self) -> str:
        return f"Activity for Scan {self.scan_result.id} at {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} - {self.action}"

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'Scan Activity'
        verbose_name_plural = 'Scan Activities'
