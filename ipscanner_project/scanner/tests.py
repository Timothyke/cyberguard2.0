from django.test import TestCase
from django.contrib.auth.models import User
from datetime import timedelta
from app_name.models import ScanResult  # Replace `app_name` with the actual app name


class ScanResultModelTest(TestCase):

    def setUp(self):
        """
        Set up common test data for the test cases.
        """
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_create_scan_result(self):
        """
        Test the creation of a ScanResult instance.
        """
        scan = ScanResult.objects.create(
            ip_address='192.168.1.1',
            result='Nmap raw output',
            status='success',
            ports=[{'port': 80, 'service': 'http'}, {'port': 443, 'service': 'https'}],
            services={'80': 'http', '443': 'https'},
            scan_duration=timedelta(seconds=30),
            scan_type='fast',
            operating_system='Linux',
            user=self.user
        )
        self.assertEqual(scan.ip_address, '192.168.1.1')
        self.assertEqual(scan.status, 'success')
        self.assertEqual(scan.scan_duration.total_seconds(), 30)
        self.assertEqual(scan.ports[0]['port'], 80)
        self.assertEqual(scan.operating_system, 'Linux')
        self.assertEqual(scan.user, self.user)

    def test_display_ports(self):
        """
        Test the display_ports method for correctly formatting open ports.
        """
        scan = ScanResult.objects.create(
            ip_address='10.0.0.1',
            result='Sample output',
            ports=[{'port': 22, 'service': 'ssh'}, {'port': 80, 'service': 'http'}]
        )
        self.assertEqual(scan.display_ports(), 'Port 22 (ssh), Port 80 (http)')

    def test_get_scan_summary(self):
        """
        Test the get_scan_summary method for generating a user-friendly summary.
        """
        scan = ScanResult.objects.create(
            ip_address='10.0.0.2',
            result='Another sample output',
            status='success',
            ports=[{'port': 8080, 'service': 'http-proxy'}],
            scan_type='full'
        )
        summary = scan.get_scan_summary()
        self.assertIn('Scan for 10.0.0.2', summary)
        self.assertIn('Status: success', summary)
        self.assertIn('Open ports: Port 8080 (http-proxy)', summary)

    def test_get_scan_duration_in_seconds(self):
        """
        Test the get_scan_duration_in_seconds method for returning scan duration in seconds.
        """
        scan = ScanResult.objects.create(
            ip_address='172.16.0.1',
            scan_duration=timedelta(minutes=2)
        )
        self.assertEqual(scan.get_scan_duration_in_seconds(), 120)

    def test_get_successful_scans(self):
        """
        Test the get_successful_scans class method.
        """
        ScanResult.objects.create(ip_address='10.1.1.1', status='success', user=self.user)
        ScanResult.objects.create(ip_address='10.1.1.2', status='failed', user=self.user)

        successful_scans = ScanResult.get_successful_scans(user=self.user)
        self.assertEqual(successful_scans.count(), 1)
        self.assertEqual(successful_scans.first().ip_address, '10.1.1.1')

    def test_get_failed_scans(self):
        """
        Test the get_failed_scans class method.
        """
        ScanResult.objects.create(ip_address='10.2.2.1', status='failed', user=self.user)
        ScanResult.objects.create(ip_address='10.2.2.2', status='success', user=self.user)

        failed_scans = ScanResult.get_failed_scans(user=self.user)
        self.assertEqual(failed_scans.count(), 1)
        self.assertEqual(failed_scans.first().ip_address, '10.2.2.1')

    def test_scan_with_null_fields(self):
        """
        Test creation of a ScanResult instance with nullable fields.
        """
        scan = ScanResult.objects.create(
            ip_address='127.0.0.1',
            result='Test result',
            status='failed'
        )
        self.assertIsNone(scan.scan_duration)
        self.assertIsNone(scan.operating_system)
        self.assertEqual(scan.status, 'failed')
