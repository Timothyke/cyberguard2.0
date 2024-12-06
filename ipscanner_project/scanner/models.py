from django.db import models
from django.contrib.auth.models import User

class ScanResult(models.Model):
    # Basic fields
    ip_address = models.GenericIPAddressField()
    scan_date = models.DateTimeField(auto_now_add=True)
    result = models.TextField()  # Store the raw output of the scan
    status = models.CharField(
        max_length=50,
        choices=[('success', 'Success'), ('failed', 'Failed')],
        default='success'
    )
    
    # Additional fields for more detailed scanning information
    ports = models.JSONField(default=list)  # List of open ports and services
    scan_duration = models.DurationField(null=True, blank=True)  # Duration of the scan
    scan_type = models.CharField(
        max_length=20,
        choices=[('fast', 'Fast Scan'), ('full', 'Full Scan')],
        default='fast'
    )
    operating_system = models.CharField(max_length=255, blank=True, null=True)  # Detected OS
    services = models.JSONField(default=list)  # Detected services per open port

    # User who initiated the scan (if user management is implemented)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    # Methods
    def __str__(self):
        return f"Scan for {self.ip_address} on {self.scan_date.strftime('%Y-%m-%d %H:%M:%S')} - {self.status}"

    # Add a method to display ports in a readable format
    def display_ports(self):
        return ', '.join([f"Port {port['port']} ({port['service']})" for port in self.ports])

    # A method to return a user-friendly description of the scan result
    def get_scan_summary(self):
        summary = f"Scan for {self.ip_address} performed on {self.scan_date.strftime('%Y-%m-%d %H:%M:%S')}. "
        summary += f"Status: {self.status}. Scan type: {self.scan_type}. "
        if self.status == 'success':
            summary += f"Open ports: {self.display_ports()}."
        else:
            summary += f"Scan failed."
        return summary

    # Method to calculate scan duration in seconds (if it's available)
    def get_scan_duration_in_seconds(self):
        if self.scan_duration:
            return self.scan_duration.total_seconds()
        return None

    # Additional method to save parsed scan result data
    def save_scan_data(self, ports, services, os_info=None):
        self.ports = ports
        self.services = services
        if os_info:
            self.operating_system = os_info
        self.save()

    # Class method to get successful scans for a specific user
    @classmethod
    def get_successful_scans(cls, user=None):
        if user:
            return cls.objects.filter(user=user, status='success')
        return cls.objects.filter(status='success')
