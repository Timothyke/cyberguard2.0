# 🛡️ Cyber Guardian Dashboard

Welcome to the **Cyber Guardian Dashboard**!  
This project provides an intuitive interface for monitoring and assessing network vulnerabilities using **Nmap**. 🚀🔍  

---

## 📜 Overview

The **Cyber Guardian Dashboard** integrates **Nmap**, a robust network scanning tool, to identify open ports and services on networked systems.  
Its goal is to help IT and cybersecurity professionals quickly assess potential vulnerabilities through a user-friendly visualization interface.

---

## 🚀 Features

- **Nmap Integration**: Seamlessly perform network scans.
- **Vulnerability Visualization**: Clear and actionable representation of scan results.
- **Real-Time Monitoring**: Keep your network secure with live status updates.
- **Customizable Scans**: Adapt scan parameters to meet specific requirements.

---

## ⚙️ Getting Started

### Prerequisites

Ensure the following are installed on your system:

1. **Python 3.x**: [Download Python](https://www.python.org/).  
2. **Flask**: Install via pip:
   ```bash
   pip install Flask
Nmap: Install using your system’s package manager:
On Kali Linux, run:
bash
Copy code
sudo apt-get install nmap
🛠️ Setup
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/cyber-guardian-dashboard.git
cd cyber-guardian-dashboard
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Configure Environment:
Ensure Nmap is installed and accessible from your system’s PATH.

🏃 Running the Application
Start the Flask Server:
Run the app on a specified port (e.g., 5001 if 5000 is in use):

bash
Copy code
python3 app.py
If you encounter a port conflict, update app.py to use a different port:

python
Copy code
app.run(debug=True, port=5001)
Access the Dashboard:
Open your browser and navigate to:

arduino
Copy code
http://127.0.0.1:5000
🧩 Project Structure
app.py: Main application file for initializing and running the Flask server.
dashboard.html: HTML template for displaying scan results.
dashboard.js: JavaScript for dynamic content and user interactions.
scanner.py: Backend script for processing scans and interfacing with Nmap.
requirements.txt: List of Python dependencies.
🔍 Example Usage
Run a Scan: Use the web interface to initiate a network scan.
View Results: Review open ports, services, and vulnerability details.
Take Action: Utilize the insights to secure your network effectively.
📝 Contributing
We welcome contributions! 🎉

To contribute:

Fork the repository.
Create a feature branch:
bash
Copy code
git checkout -b feature-name
Submit a pull request with a detailed description of your changes.
📧 Contact
For inquiries, suggestions, or support, feel free to reach out:

Email: timothymaina040@gmail.com
Phone/WhatsApp: +254794637463
