# FailTrace – SOC Log Analysis Project

## About the Project
FailTrace is a project built in Kali Linux that detects failed SSH login attempts. 
It reads Linux authentication logs, counts failed login attempts, and generates a clear incident report.

The project demonstrates basic SOC (Security Operations Center) skills, such as monitoring logs, detecting suspicious activity, and documenting incidents.

---

## How It Works
1. The script reads a log file (`failtrace_auth.log` or `/var/log/auth.log`). 
2. It looks for failed SSH login attempts. 
3. Counts the number of failed attempts per IP address. 
4. Generates a report (`failtrace_report.txt`) showing:
   - Suspicious IP address 
   - Number of failed attempts 
   - Severity (Low / Medium / High) 
   - Possible attack type (Brute Force)

---

## Tools & Technologies
- Kali Linux 
- Python 3 
- Linux Authentication Logs (`auth.log`) 
- SSH for generating test login failures 

---

## Sample Output
FailTrace Incident Report

Incident Type: Failed SSH Login Attempts
Log Source: Custom Filtered Log

Suspicious IP Address: 127.0.0.1
Failed Attempts: 3
Severity: Medium
Possible Attack: Brute Force

## What I Learned
- How to analyze Linux authentication logs 
- Basic Python scripting for cybersecurity tasks 
- How SOC analysts detect suspicious logins 
- Importance of accurate and evidence-based incident reporting 
- Generating automated reports for security monitoring 

---

## Author
**Pushkar Kiran Shete** 
B.Sc Cybersecurity – 1st Year
