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
        # Execute the nmap command
        result = subprocess.run(
            ["nmap", "-F", ip],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
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
        if "open" in line:
            parts = line.split()
            try:
                port = parts[0]
                service = parts[2] if len(parts) > 2 else "Unknown Service"
                parsed_results[port] = service
            except IndexError:
                continue  # Handle unexpected line format

    return parsed_results
