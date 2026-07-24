# 🔐 Password Security Analyzer

A Python-based Password Security Analyzer that evaluates password strength using multiple security parameters. The application provides a graphical user interface (GUI), password analysis, entropy calculation, crack time estimation, password suggestions, strong password generation, and PDF report export.

---

## Features

- Password Length Validation
- Uppercase Letter Check
- Lowercase Letter Check
- Number Check
- Special Character Check
- Common Password Detection
- Password Strength Scoring
- Password Entropy Calculation
- Estimated Crack Time
- Password Improvement Suggestions
- Strong Password Generator
- GUI using Tkinter
- Export Analysis Report as PDF

---

## Technologies Used

- Python 3
- Tkinter
- ReportLab
- Math Module
- Random Module
- String Module

---

## Project Structure

```
PasswordSecurityAnalyzer/

│── analyzer.py
│── gui.py
│── pdf_export.py
│── main.py
│── common_passwords.txt
│── requirements.txt
│── README.md

├── reports/
├── screenshots/
├── assets/
├── logs/
```

---

## How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run GUI

```bash
python gui.py
```

---

## Sample Output

The application displays:

- Password Score
- Password Strength
- Password Entropy
- Estimated Crack Time
- Suggestions
- Strong Password Generator
- Export PDF Report

---
## Screenshots

### Home Screen
![Home Screen](screenshots/home_screen.png)

### Weak Password
![Weak Password](screenshots/weak_password.png)

### Medium Password
![Medium Password](screenshots/medium_password.png)

### Strong Password
![Strong Password](screenshots/strong_password.png)

### Generated Password
![Generated Password](screenshots/generated_password.png)
---

## Author

Sanika Patil

MCA Student

Python Security Project
