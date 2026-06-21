# Student Cyber Security Management System

A menu-driven Python application developed as part of the internship final project. The system manages student records and provides basic cyber security utilities such as security assessment, password strength checking, and username generation.

---

## Objective

This project combines the core programming concepts learned during the internship:

- Variables
- Input / Output
- Conditional Statements
- Loops
- Functions
- Lists
- File Handling
- Problem Solving

The application stores student records, performs security assessments, and generates reports through a simple command-line interface.

---

## Features

### Student Management

#### Add Student
Store the following details:
- Student ID
- Student Name
- Branch
- Email Address

#### View Students
Display all stored student records.

#### Search Student
Search students using:
- Student ID
- Student Name

#### Delete Student
Remove a student record from storage.

---

### Security Assessment

Evaluates a student's security practices based on:

- Multi-Factor Authentication (MFA)
- Password Length
- System Updates
- Antivirus Installation

Generates:
- Security Score (0–100)
- Security Status

Categories:
- Excellent
- Good
- Moderate
- Poor

---

### Report Generation

Generates a summary report containing:

- Total Students
- Security Scores
- Average Security Score
- Students with Poor Security Ratings

---

### Cyber Security Tools

#### Password Strength Checker
Analyzes password complexity and classifies it as:

- Strong
- Medium
- Weak

#### Username Generator
Automatically generates a username from a user's full name.

#### Login Validation
Provides basic authentication before accessing the system.

Default Credentials:

```text
Username: admin
Password: admin123
```

---

## File Storage

Student records are stored in:

```text
students.txt
```

Supported operations:

- Save Records
- Read Records
- Delete Records

---

## Project Structure

```text
Final_Project/
│
├── student_security_manager.py
├── students.txt
├── screenshot/
│   ├── Screenshot 1.png
│   ├── Screenshot 2.png
│   └── ...
└── README.md
```

---

## Sample Menu

```text
==========================
 Student Security Manager
==========================

1. Add Student
2. View Students
3. Search Student
4. Delete Student
5. Security Assessment
6. Generate Report
7. Cyber Security Tools
8. Exit
```

---

## Screenshots

### Login

![Login](screenshot/Screenshot%202026-06-21%20202231.png)

### View Students

![View Students](screenshot/Screenshot%202026-06-21%20202335.png)

### Search Student

![Search Student](screenshot/Screenshot%202026-06-21%20202400.png)

### Delete Student

![Delete Student](screenshot/Screenshot%202026-06-21%20202424.png)

### Security Assessment

![Security Assessment](screenshot/Screenshot%202026-06-21%20202821.png)

### Generate Report

![Generate Report](screenshot/Screenshot%202026-06-21%20202850.png)

### Cyber Security Tools

![Cyber Tools](screenshot/Screenshot%202026-06-21%20203036.png)


### Exit the program

![Exit](screenshot/Screenshot%202026-06-21%20203058.png)

---

## Technologies Used

- Python 3
- File Handling
- Command Line Interface (CLI)


