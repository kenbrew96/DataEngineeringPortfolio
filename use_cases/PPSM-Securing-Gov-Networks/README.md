# 🔌 Port, Protocol, and Service Management (PPSM): Securing Maryland Government Networks

## 📌 Project Overview
The Maryland state government requires **strict network security controls** to protect against cyber threats. This project **implements Port, Protocol, and Service Management (PPSM)** to limit network exposure and enforce security best practices.

By analyzing **open ports, allowed protocols, and active services**, this initiative ensures only **essential services** remain accessible while reducing attack surfaces.

---

## 📊 Network Security Assessment
- **Risk Areas:** Unauthorized services, unprotected open ports, outdated protocols.
- **Assessment Tools:** Nmap, Wireshark, Netstat.
- **Security Categories:**
  | Security Measure | Implementation Status |
  |------------------|----------------------|
  | Close unnecessary ports | ✅ Completed |
  | Restrict outdated protocols (TLS 1.0, FTP) | ✅ Implemented |
  | Monitor active network services | ✅ Ongoing |

---

## 🛠️ Steps Implemented
1. **Scan Network for Open Ports:** Identify potential security risks.
2. **Restrict Access:** Block unused or vulnerable services.
3. **Enforce Secure Protocols:** Allow only encrypted traffic for data transmission.
4. **Monitor & Audit:** Continuously log and review network activity.

---

## 🚀 Technologies Used
- 🌐 **Nmap & Wireshark** – Network scanning and traffic analysis.
- 🔐 **IPTables & FirewallD** – Configuring port and protocol restrictions.
- 📡 **SIEM & Log Monitoring** – Real-time network security tracking.

---

## 🔧 How to Secure Network Services

### **1️⃣ Scan for Open Ports (Nmap Example)**
```sh
nmap -p- -sV 192.168.1.1
```

### **2️⃣ Restrict Unused Ports (Linux IPTables Example)**
```sh
sudo iptables -A INPUT -p tcp --dport 23 -j DROP  # Block Telnet
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT  # Allow HTTP
```

### **3️⃣ Monitor Network Traffic (Wireshark Example)**
```sh
tshark -i eth0 -f "port 22"
```

### **4️⃣ Configure PPSM Rules in `configure_ports.py`**
Create a Python script to automate port restrictions:
```python
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
```
Run the script:
```sh
python configure_ports.py
```

After implementing these security measures, **only necessary services remain accessible**, ensuring a secure government network.

---

## 📊 Expected Security Enhancements
| Security Feature | Implementation Status |
|-----------------|----------------------|
| Block Unused Ports | ✅ Completed |
| Enforce Secure Protocols | ✅ Implemented |
| Real-Time Monitoring | ✅ Active |

---

## 🏆 Key Skills Demonstrated
✅ **Performing network security assessments**  
✅ **Enforcing port and protocol restrictions**  
✅ **Using security tools to monitor threats**  

---

## 🔍 Next Steps
🔹 **Automate firewall rule enforcement with Ansible.**  
🔹 **Integrate network security monitoring with SIEM solutions.**  
🔹 **Conduct periodic compliance audits.**  

---

## 🤝 Contributing
Contributions are welcome! Feel free to **enhance network policies, refine firewall rules, or integrate with advanced threat detection systems.**


