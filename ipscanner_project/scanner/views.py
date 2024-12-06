import subprocess
import re
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Function to validate IP address format
def is_valid_ip(ip):
    pattern = re.compile(r"^(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}$")
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

# Home page view (scanner page) with login required
@login_required
def scanner_page(request):
    if request.method == 'POST':
        ip = request.POST.get('ip')

        if not ip:
            return JsonResponse({"error": "No IP provided"}, status=400)

        if not is_valid_ip(ip):
            return JsonResponse({"error": "Invalid IP address provided"}, status=400)

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
                return JsonResponse({"error": f"nmap scan failed: {result.stderr.strip()}"}, status=500)

            # Parse nmap output for useful data (open ports and services)
            parsed_results = parse_nmap_output(result.stdout.splitlines())

            # If no open ports are found
            if not parsed_results:
                return JsonResponse({"ip": ip, "message": "No open ports found"}, status=200)

            # Return parsed results as JSON
            return JsonResponse({"ip": ip, "open_ports": parsed_results})

        except subprocess.CalledProcessError as e:
            return JsonResponse({"error": f"Error while executing nmap: {str(e)}"}, status=500)

        except Exception as e:
            return JsonResponse({"error": f"Unexpected error: {str(e)}"}, status=500)

    return render(request, 'scanner/scanner_page.html')

# Login view to handle user login
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('scanner_page')  # Redirect to the scanner page after successful login
        else:
            return render(request, 'scanner/login.html', {'error': 'Invalid username or password'})

    return render(request, 'scanner/login.html')  # Render the login page for GET requests
