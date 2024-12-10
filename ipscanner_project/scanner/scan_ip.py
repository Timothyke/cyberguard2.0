import subprocess
import re


def is_valid_ip(ip):
    """
    Validate the given IP address using regex for IPv4 format.
    """
    pattern = re.compile(
        r"^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])"
        r"(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}$"
    )
    return bool(pattern.match(ip))


def scan_ip(ip):
    """
    Perform an nmap scan on the given IP address.
    """
    try:
        # Check if IP is valid
        if not is_valid_ip(ip):
            raise ValueError(f"Invalid IP address: {ip}")

        # Execute the nmap command
        result = subprocess.run(
            ["nmap", "-F", ip],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=30,  # Set a timeout for the scan
        )

        # Check for errors
        if result.returncode != 0:
            raise RuntimeError(f"nmap scan failed: {result.stderr.strip()}")

        return result.stdout
    except Exception as e:
        raise RuntimeError(f"Error scanning IP: {e}")


def parse_nmap_output(output):
    """
    Parse nmap output to extract open ports and services.
    """
    parsed_results = {}

    for line in output.splitlines():
        if "open" in line:  # Only look at lines mentioning "open"
            parts = line.split()
            try:
                port = parts[0]
                service = parts[2] if len(parts) > 2 else "Unknown Service"
                parsed_results[port] = service
            except IndexError:
                continue  # Handle unexpected line format

    return parsed_results


# Example Usage
ip_to_scan = "192.168.1.1"
if is_valid_ip(ip_to_scan):
    try:
        nmap_output = scan_ip(ip_to_scan)
        parsed_ports = parse_nmap_output(nmap_output)
        print(parsed_ports)  # Display open ports and services
    except Exception as e:
        print(f"Error: {e}")
else:
    print(f"Invalid IP address: {ip_to_scan}")
