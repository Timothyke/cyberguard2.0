🛡️ Cyber Guardian Dashboard
Welcome to the Cyber Guardian Dashboard!
This project provides an intuitive interface for monitoring and assessing network vulnerabilities using Nmap. 🚀🔍

📜 Overview
The Cyber Guardian Dashboard integrates Nmap, a robust network scanning tool, to identify open ports and services on networked systems.
Its goal is to help IT and cybersecurity professionals quickly assess potential vulnerabilities through a user-friendly visualization interface.

🚀 Features
Login System: Secure access to the dashboard using Django’s built-in authentication.
Nmap Integration: Seamlessly perform network scans.
Vulnerability Visualization: Clear and actionable representation of scan results.
Real-Time Monitoring: Keep your network secure with live status updates.
Customizable Scans: Adapt scan parameters to meet specific requirements.
⚙️ Getting Started
Prerequisites
Ensure the following are installed on your system:

Python 3.x: Download Python.
Django: Install via pip:
bash
Copy code
pip install Django
Nmap: Install using your system’s package manager:
On Kali Linux, run:
bash
Copy code
sudo apt-get install nmap
🛠️ Setup
Clone the Repository:

bash
Copy code
git clone https://github.com/Timothyke/cyber-guardian-dashboard.git
cd cyber-guardian-dashboard
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Configure Environment:
Ensure Nmap is installed and accessible from your system’s PATH.

Apply Migrations:
Set up the database for user authentication and scan storage:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Create a Superuser:
Access the admin panel to manage users and scan data:

bash
Copy code
python manage.py createsuperuser
🏃 Running the Application
Start the Django Server:
Run the app:

bash
Copy code
python manage.py runserver
Access the Dashboard:
Open your browser and navigate to:

arduino
Copy code
http://127.0.0.1:8000/
🔒 About the Login Page
The Cyber Guardian Dashboard includes a secure login system to restrict access to authorized users only.

Login Features:
User Authentication: Users must log in to access the scanner and view results.
Django Admin Integration: Manage users, scans, and other data through the admin panel.
Session Security: Ensures that users are logged out after a session timeout or manual logout.
Accessing the Login Page:
Navigate to the login page at:
arduino
Copy code
http://127.0.0.1:8000/login/
Enter your username and password to log in. If you don’t have an account, contact your administrator for access.
Logout:
To securely exit the dashboard, click the Logout button on the scanner page.
🧩 Project Structure
app.py: Main application logic for running scans (Flask version for reference).
scanner/: Django app handling scan logic, views, and templates:
views.py: Handles user requests and scanner functionality.
models.py: Defines the database structure for storing scan results.
urls.py: App-specific URL routing.
templates/scanner/: HTML templates for the login page and scanner dashboard.
static/: Contains CSS and JavaScript for the frontend.
requirements.txt: List of Python dependencies.
🔍 Example Usage
Log In: Navigate to the login page and authenticate.
Run a Scan: Use the web interface to initiate a network scan.
View Results: Review open ports, services, and vulnerability details.
Take Action: Utilize the insights to secure your network effectively.
📝 Contributing
We value your contributions and ideas to improve this project! 🎉

To contribute:

Fork the Repository: Create your copy of the project.
Create a Feature Branch:
bash
Copy code
git checkout -b your-feature-name
Submit a Pull Request: Provide a detailed description of your changes and their purpose.
Let’s make this project even better together!

📧 Contact
Have questions, suggestions, or need support? Feel free to reach out:

Email: timothymaina040@gmail.com
Phone/WhatsApp: +254 794 637 463
We’re here to help secure your network! 🛡️

