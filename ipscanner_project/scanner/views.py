from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .scan_ip import scan_ip as perform_scan, is_valid_ip, parse_nmap_output  # Import custom functions


def scan_ip(request):
    """
    Handle the actual scanning of IP addresses.
    """
    if request.method == 'POST':
        ip = request.POST.get('ip')

        # Validate the IP address
        if not ip:
            return JsonResponse({"error": "No IP address provided"}, status=400)

        if not is_valid_ip(ip):
            return JsonResponse({"error": "Invalid IP address"}, status=400)

        try:
            # Perform the scan
            output = perform_scan(ip)  # Use scan_ip from scan_ip.py
            parsed_results = parse_nmap_output(output)  # Parse results

            if not parsed_results:
                return JsonResponse({"ip": ip, "message": "No open ports found"}, status=200)

            return JsonResponse({"ip": ip, "open_ports": parsed_results}, status=200)

        except RuntimeError as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=400)


# Login View
def user_login(request):
    """
    Handle user login and authentication.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('scanner_page')  # Redirect to scanner page on success
        else:
            # Render login page with an error message for failed login
            return render(request, 'scanner/login.html', {'error': 'Invalid username or password'})

    # Render login page for GET requests
    return render(request, 'scanner/login.html')


# Scanner Page View
@login_required
def scanner_page(request):
    """
    Render the scanner page and handle IP scan requests.
    """
    if request.method == 'POST':
        ip = request.POST.get('ip')

        # Validate the IP address
        if not ip:
            return JsonResponse({"error": "No IP address provided"}, status=400)

        if not is_valid_ip(ip):
            return JsonResponse({"error": "Invalid IP address"}, status=400)

        try:
            # Perform the scan
            output = perform_scan(ip)  # Use scan_ip function from scan_ip module
            parsed_results = parse_nmap_output(output)  # Parse nmap results

            # Return results or indicate no open ports
            if not parsed_results:
                return JsonResponse({"ip": ip, "message": "No open ports found"}, status=200)

            return JsonResponse({"ip": ip, "open_ports": parsed_results}, status=200)

        except RuntimeError as e:
            return JsonResponse({"error": str(e)}, status=500)

    # Render scanner page for GET requests
    return render(request, 'scanner/scanner_page.html')
