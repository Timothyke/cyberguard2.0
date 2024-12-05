
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
   ```
3. **Nmap**: Install using your system’s package manager:  
   On **Kali Linux**, run:
   ```bash
   sudo apt-get install nmap
   ```

---

### 🛠️ Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Timothyke/cyber-guardian-dashboard.git
   cd cyber-guardian-dashboard
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment**:  
   Ensure **Nmap** is installed and accessible from your system’s `PATH`.

---

## 🏃 Running the Application

1. **Start the Flask Server**:  
   Run the app on a specified port (e.g., `5001` if `5000` is in use):
   ```bash
   python3 app.py
   ```
   If you encounter a port conflict, update `app.py` to use a different port:
   ```python
   app.run(debug=True, port=5001)
   ```

2. **Access the Dashboard**:  
   Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

---

## 🧩 Project Structure

- **`app.py`**: Main application file for initializing and running the Flask server.
- **`dashboard.html`**: HTML template for displaying scan results.
- **`dashboard.js`**: JavaScript for dynamic content and user interactions.
- **`scanner.py`**: Backend script for processing scans and interfacing with Nmap.
- **`requirements.txt`**: List of Python dependencies.

---

## 🔍 Example Usage

1. **Run a Scan**: Use the web interface to initiate a network scan.  
2. **View Results**: Review open ports, services, and vulnerability details.  
3. **Take Action**: Utilize the insights to secure your network effectively.

---

## 📝 Contributing

We value your contributions and ideas to improve this project! 🎉  

To contribute:  
1. **Fork the Repository**: Create your copy of the project.  
2. **Create a Feature Branch**:  
   ```bash
   git checkout -b your-feature-name
   ```  
3. **Submit a Pull Request**: Provide a detailed description of your changes and their purpose.

Let’s make this project even better together!

---

## 📧 Contact

Have questions, suggestions, or need support? Feel free to reach out:  

- **Email**: [timothymaina040@gmail.com](mailto:timothymaina040@gmail.com)  
- **Phone/WhatsApp**: [+254 794 637 463](tel:+254794637463)  

We’re here to help secure your network! 🛡️  
```
