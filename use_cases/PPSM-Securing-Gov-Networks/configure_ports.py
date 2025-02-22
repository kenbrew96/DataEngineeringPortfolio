import os

# Define ports to allow and deny
allowed_ports = [80, 443]
denied_ports = [23, 21, 25]

# Apply firewall rules
for port in denied_ports:
    os.system(f"sudo iptables -A INPUT -p tcp --dport {port} -j DROP")

for port in allowed_ports:
    os.system(f"sudo iptables -A INPUT -p tcp --dport {port} -j ACCEPT")

print("✅ PPSM security rules applied successfully.")
