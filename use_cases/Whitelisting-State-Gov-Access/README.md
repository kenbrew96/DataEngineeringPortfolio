# ✅ Whitelisting Security: Maryland State Government Access Control

## 📌 Project Overview
The Maryland state government requires **strict access control** to prevent unauthorized access to sensitive systems.

This project **implements IP-based and software whitelisting** to ensure only approved users and applications can access government infrastructure.

---

## 📊 Dataset
- **File:** `whitelist_rules.conf`
- **Contents:** Predefined whitelisting rules for network and software access.
- **Sample Data:**
  ```conf
  # Allow government office IPs
  allow from 203.0.113.0/24
  # Allow specific applications
  allow application gov-secure-app
  ```

---

## 🛠️ Steps Implemented
1. **Define Whitelisting Policies:** Approve only trusted IPs and applications.
2. **Configure Whitelisting Rules:** Implement network and software-level restrictions.
3. **Test & Monitor:** Ensure only authorized users can access systems.

---

## 🚀 Technologies Used
- 🔐 **IPTables & UFW** – IP-based whitelisting.
- 🖥️ **Windows AppLocker & Linux AppArmor** – Software whitelisting.
- 📡 **Network Access Control (NAC)** – Enforcing security policies.

---

## 🔧 How to Configure

### **1️⃣ Set Up IP Whitelisting (Linux UFW)**
```sh
sudo ufw allow from 203.0.113.0/24
sudo ufw enable
```

### **2️⃣ Configure Software Whitelisting (Windows AppLocker)**
1. Open **Local Security Policy** (`secpol.msc`).
2. Navigate to **Application Control Policies > AppLocker**.
3. Define rules to **allow only government-approved applications**.

### **3️⃣ Automate Whitelisting in `ip_whitelisting.py`**
Create a Python script to enforce IP whitelisting:
```python
import os

def apply_whitelist():
    os.system("sudo ufw allow from 203.0.113.0/24")
    os.system("sudo ufw enable")
    print("✅ Whitelist rules applied successfully.")

if __name__ == "__main__":
    apply_whitelist()
```
Run the script:
```sh
python ip_whitelisting.py
```

After configuring whitelisting, only **approved government employees and applications** will have system access.

---

## 📊 Expected Rules
| Rule Type  | Whitelisted Entity        | Action  |
|------------|--------------------------|---------|
| IP-Based   | 203.0.113.0/24            | ✅ Allow |
| Software   | gov-secure-app            | ✅ Allow |
| Default    | All Other Apps/Users      | ❌ Deny  |

---

## 🏆 Key Skills Demonstrated
✅ **Configuring IP and software whitelisting**  
✅ **Implementing strict access control policies**  
✅ **Monitoring security logs for unauthorized access**  

---

## 🔍 Next Steps
🔹 **Automate security audits using scripts.**  
🔹 **Enhance logging and alerting for unauthorized attempts.**  
🔹 **Integrate whitelisting with multi-factor authentication (MFA).**  

---

## 🤝 Contributing
Contributions are welcome! Feel free to **improve automation, enhance security policies, or integrate with cloud access control solutions.**


