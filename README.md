

---

# 🛡️ **Cyber Guardian Dashboard**

Welcome to the **Cyber Guardian Dashboard**!  
This project provides an intuitive interface for monitoring and assessing network vulnerabilities using **Nmap**. 🚀🔍  

---

## 📜 **Overview**

The **Cyber Guardian Dashboard** integrates **Nmap**, a robust network scanning tool, to identify open ports and services on networked systems.  
Its goal is to help IT and cybersecurity professionals quickly assess potential vulnerabilities through a user-friendly visualization interface.

---

## 🚀 **Features**

- **🔒 Login System**: Secure access using Django’s built-in authentication.
- **🌐 Nmap Integration**: Perform seamless network scans for vulnerabilities.
- **📊 Vulnerability Visualization**: Clear and actionable representation of scan results.
- **⏱️ Real-Time Monitoring**: Live updates for network status.
- **⚙️ Customizable Scans**: Flexible scan parameters to suit specific needs.

---

## ⚙️ **Getting Started**

### **Prerequisites**

Ensure the following are installed on your system:

1. **Python 3.x**: [Download Python](https://www.python.org/).  
2. **Django**: Install via pip:
   ```bash
   pip install Django
   ```
3. **Nmap**: Install using your system’s package manager:  
   On **Kali Linux**, run:
   ```bash
   sudo apt-get install nmap
   ```

---

### 🛠️ **Setup**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Timothyke/cyber-guardian-dashboard.git
   cd cyber-guardian-dashboard
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Apply Migrations**:  
   Set up the database for user authentication and scan storage:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create a Superuser**:  
   Access the admin panel to manage users and scan data:
   ```bash
   python manage.py createsuperuser
   ```

5. **Configure Environment**:  
   Ensure **Nmap** is installed and accessible from your system’s `PATH`.

---

## 🏃 **Running the Application**

1. **Start the Django Server**:  
   Run the app:
   ```bash
   python manage.py runserver
   ```

2. **Access the Dashboard**:  
   Open your browser and navigate to:
   ```
   http://127.0.0.1:8000/
   ```

---

## 🔒 **Login Page**

The Cyber Guardian Dashboard includes a secure login system to restrict access to authorized users only.

### **Login Features**
- **User Authentication**: Users must log in to access the scanner and view results.
- **Django Admin Integration**: Manage users, scans, and other data through the admin panel.
- **Session Security**: Ensures that users are logged out after a session timeout or manual logout.

### **Accessing the Login Page**
1. Navigate to the login page at:
   ```
   http://127.0.0.1:8000/login/
   ```
2. Enter your username and password to log in. If you don’t have an account, contact your administrator for access.

### **Logout**
- To securely exit the dashboard, click the **Logout** button on the scanner page.

---

## 📂 **Project Structure**

```
ipscanner_project/
├── ipscanner_project/       # Main project directory
│   ├── settings.py
│   ├── urls.py
│   ├── ...
├── scanner/                 # Django app for scanning
│   ├── templates/           # HTML templates
│   │   ├── scanner/
│   │       ├── scanner_page.html
│   ├── static/              # Static files like CSS and JS
│   │   ├── styles.css
│   ├── views.py             # Contains app logic for scanning
│   ├── models.py            # Database models for scan storage
│   ├── urls.py              # App-specific URL routing
├── manage.py
```

---

## 🔍 **Example Usage**

1. **Log In**: Navigate to the login page and authenticate.
2. **Run a Scan**: Use the web interface to initiate a network scan.  
3. **View Results**: Review open ports, services, and vulnerability details.  
4. **Take Action**: Utilize the insights to secure your network effectively.

---

## 📝 **Contributing**

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

## 📧 **Contact**

Have questions, suggestions, or need support? Feel free to reach out:

- **Email**: [timothymaina040@gmail.com](mailto:timothymaina040@gmail.com)  
- **Phone/WhatsApp**: [+254 794 637 463](tel:+254794637463)  

We’re here to help secure your network! 🛡️  

---


