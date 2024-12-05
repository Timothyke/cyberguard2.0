from flask import Flask, render_template, request, jsonify
import subprocess
import re

app = Flask(__name__)

# Function to validate IP address format
def is_valid_ip(ip):
    pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    return bool(pattern.match(ip))

# Function to parse nmap output and extract useful information
def parse_nmap_output(output):
    parsed_results = {}
    
    # Parse open ports and services from nmap output
    for line in output:
        if "open" in line:
            parts = line.split()
            port = parts[0]
            service = parts[2] if len(parts) > 2 else "Unknown Service"
            parsed_results[port] = service

    return parsed_results

@app.route('/')
def home():
    # Render the scanner page
    return render_template('scanner.html')

@app.route('/scan', methods=['POST'])
def scan():
    ip = request.form.get('ip')  # Get the IP address from the form
    if not ip:
        return jsonify({"error": "No IP provided"}), 400

    if not is_valid_ip(ip):
        return jsonify({"error": "Invalid IP address provided"}), 400

    try:
        # Run nmap scan on the provided IP address
        result = subprocess.run(
            ["nmap", "-F", ip],  # "-F" is for a fast scan of common ports
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # If nmap fails
        if result.returncode != 0:
            return jsonify({"error": f"nmap scan failed: {result.stderr.strip()}"}), 500

        # Parse nmap output for useful data (open ports and services)
        parsed_results = parse_nmap_output(result.stdout.splitlines())

        # If no open ports are found
        if not parsed_results:
            return jsonify({"ip": ip, "message": "No open ports found"}), 200

        # Return parsed results as JSON
        return jsonify({"ip": ip, "open_ports": parsed_results})

    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
