import datetime

log_file = "failtrace_auth.log"
report_file = "failtrace_report.txt"
THREESHOLD = 3

failed_attempts = {}
total_lines_processed = 0

print("FailTrace: Starting SOC Log Analysis...")

with open(log_file, "r") as file:
    for line in file:
        total_lines_processed += 1
        if "Failed password" in line:
            parts = line.split()
            if "from" in parts:
                ip_address = parts[parts.index("from") + 1]
                failed_attempts[ip_address] = failed_attempts.get(ip_address, 0) +1

with open(report_file, "w") as report:
    report.write("FailTrace Incident Report\n")
    report.write("Incident Type: Failed SSH Login Attempts\n")
    report.write("Log Source: Custom Filtered Log\n\n")

    if not failed_attempts:
        report.write("No failed login attempts detected.\n")
    else:
        for ip, count in failed_attempts.items():
            if count >= THREESHOLD:
                report.write(f"Suspicious IP Address: {ip}\n")
                report.write(f"Failed Attempts: {count}\n")
                report.write("Severity: Medium\n")
                report.write("Possible Attack: Brute Force\n\n")

print("Analysis complete.")
print("Report generated: failtrace_report.txt")
