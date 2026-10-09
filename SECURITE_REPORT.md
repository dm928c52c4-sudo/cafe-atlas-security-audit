# Security Audit Report - Café Atlas
**Author:** Ethical Hacker from Marrakech
**Date:** Oct 2026
**Target:** http://127.0.0.1:5000 (Local Test Environment - Legal)

### 1. Project Description
Café Atlas is a Flask-based web application simulating a real café menu in Marrakech. Built for educational cybersecurity training.

### 2. Methodology (White Hat - 100% Legal)
- Built a local web server with Python Flask
- Performed Port Scanning (4900-5100)
- Performed Directory Bruteforce

### 3. Tools Used
- Python, Flask, Socket, Requests library
- Custom Scanner (scanner.py)
- Custom Finder (finder.py)

### 4. Findings
- **Port 5000:** OPEN -> Flask application running. Expected and secure.
- **Port 5040:** OPEN -> Windows service, not related to app.
- **Paths:** /admin, /login, /dashboard, /api -> NOT FOUND (404). Good security practice, no exposed admin panels.

### 5. Conclusion & Recommendations
The application does not expose sensitive admin pages. For production, recommend:
- Add HTTPS
- Add login rate-limiting
- Hide server version headers

**Status: SECURE for this level**