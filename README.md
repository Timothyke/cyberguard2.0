# 🛡️ Cyber Guardian Dashboard

Welcome to the **Cyber Guardian Dashboard**! This project is designed to provide an intuitive interface for monitoring and assessing network vulnerabilities using Nmap. 🚀🔍

## 📜 Overview

The **Cyber Guardian Dashboard** integrates Nmap, a powerful network scanning tool, to detect open ports and services on networked systems. The dashboard visualizes scan results, helping you stay informed about potential security vulnerabilities in your network. 

## 🚀 Features

- **Nmap Integration**: Perform network scans using Nmap.
- **Vulnerability Visualization**: View scan results in an easy-to-understand format.
- **Real-Time Monitoring**: Monitor network status and vulnerabilities in real-time.
- **Customizable Scans**: Configure scan parameters and targets as needed.

## ⚙️ Getting Started

### Prerequisites

Before running the application, ensure you have the following installed:

- **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- **Flask**: Install Flask via pip:
  ```bash
  pip install Flask
  ```
- **Nmap**: Ensure Nmap is installed on your system. Install Nmap on Kali Linux using:
  ```bash
  sudo apt-get install nmap
  ```

### 🛠️ Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/cyber-guardian-dashboard.git
   cd cyber-guardian-dashboard
   ```

2. **Install Dependencies**:
   Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Your Environment**:
   Make sure Nmap is correctly installed and accessible from your PATH.

### 🏃 Running the Application

1. **Start the Flask Server**:
   If port 5000 is in use, you can specify a different port. Here’s how to run it on port 5001:
   ```bash
   python3 app.py
   ```
   If you encounter an "Address already in use" error, you might need to stop other processes using port 5000, or you can modify the `app.py` to use a different port (e.g., `app.run(debug=True, port=5001)`).

2. **Access the Dashboard**:
   Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## 🧩 Project Structure

- **`app.py`**: Main application file that initializes and runs the Flask server.
- **`keylogger.html`**: HTML template for displaying scan results.
- **`keylogger.js`**: JavaScript for handling dynamic content and user interactions.
- **` keylogger.py2`**: Python script for handling backend processes and interactions.
- **`requirements.txt`**: Lists Python dependencies.

## 🔍 Example Usage

1. **Run a Scan**: Trigger a scan using the web interface.
2. **View Results**: Check the results displayed on the dashboard.
3. **Analyze Data**: Use the data to identify and mitigate potential vulnerabilities.

## 📝 Contributing

Contributions are welcome! If you have suggestions, improvements, or bug fixes, please submit a pull request or open an issue.

## 📧 Contact

For any questions or support, feel free to reach out:

- **Email**:timothymaina040@gmail.com
- **Phone/WhatsApp**:0794637463
