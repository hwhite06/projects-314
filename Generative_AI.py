import re

def extract_ip_addresses(log_entries):
    # Regular expression pattern for matching IPv4 addresses
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    
    ip_addresses = []
    
    for entry in log_entries:
        # Find all matching IP addresses in the log entry
        matches = re.findall(ip_pattern, entry)
        ip_addresses.extend(matches)
    
    return ip_addresses

# Example log entries
log_entries = [
    "User from 192.168.1.1 accessed the system.",
    "Failed login attempt from 10.0.0.1.",
    "Connection established from 172.16.254.1.",
    "Invalid request from 256.100.50.25",  # Invalid IP
    "Access granted to 192.168.1.10 and 10.0.0.5."
]

# Extract IP addresses
ip_addresses = extract_ip_addresses(log_entries)

# Print the results
print("Extracted IP Addresses:")
for ip in ip_addresses:
    print(ip)