# 🔐 Access Control Lists (ACLs): Maryland University Library System

## 📌 Project Overview
The Maryland University Library requires **strict access control** to regulate permissions for students, faculty, and guests.

This project **implements Access Control Lists (ACLs)** to manage user access based on roles, ensuring security and proper data access.

---

## 📊 Dataset
- **File:** `acl_rules.conf`
- **Contents:** Predefined ACL rules for different user roles.
- **Sample Data:**
  ```conf
  # Allow faculty full access
  user faculty allow all
  # Allow students read-only access
  user student allow read
  # Restrict guest access
  user guest deny all
  ```

---

## 🛠️ Steps Implemented
1. **Define Role-Based Permissions:** Assign access based on user type.
2. **Configure ACL Rules:** Implement read/write restrictions for different roles.
3. **Test & Monitor:** Validate access control settings and log unauthorized attempts.

---

## 🚀 Technologies Used
- 🔑 **Linux ACLs (setfacl, getfacl)** – File and directory permissions.
- 🔧 **Windows NTFS Permissions** – Role-based access control.
- 📡 **Network ACLs (AWS, Cisco)** – Restricting network resource access.

---

## 🔧 How to Configure

### **1️⃣ Set Up File System ACLs (Linux)**
```sh
sudo setfacl -m u:faculty:rwx /library_resources
sudo setfacl -m u:student:r-- /library_resources
sudo setfacl -m u:guest:--- /library_resources
```

### **2️⃣ Configure Network ACLs (AWS Example)**
```sh
aws ec2 create-network-acl-entry --network-acl-id acl-12345 \
  --ingress --rule-number 100 --protocol tcp --port-range From=80,To=80 \
  --cidr-block 192.168.1.0/24 --rule-action allow
```

### **3️⃣ Automate ACL Configuration in `acl_permissions.py`**
Create a Python script to automate ACL rule setup:
```python
import os

def apply_acl():
    os.system("sudo setfacl -m u:faculty:rwx /library_resources")
    os.system("sudo setfacl -m u:student:r-- /library_resources")
    os.system("sudo setfacl -m u:guest:--- /library_resources")
    print("✅ ACL rules applied successfully.")

if __name__ == "__main__":
    apply_acl()
```
Run the script:
```sh
python acl_permissions.py
```

After applying these ACLs, **faculty members will have full access**, **students will have read-only permissions**, and **guests will be restricted**.

---

## 📊 Expected ACL Rules
| User Role | Permissions      | Resource           |
|-----------|----------------|-------------------|
| Faculty   | Full Access     | /library_resources |
| Student   | Read-Only       | /library_resources |
| Guest     | No Access       | /library_resources |

---

## 🏆 Key Skills Demonstrated
✅ **Implementing role-based access control**  
✅ **Using ACLs to enforce security policies**  
✅ **Monitoring unauthorized access attempts**  

---

## 🔍 Next Steps
🔹 **Automate ACL rule enforcement with scripts.**  
🔹 **Enhance logging for better security auditing.**  
🔹 **Integrate ACLs with identity and access management (IAM) systems.**  

---

## 🤝 Contributing
Contributions are welcome! Feel free to **improve automation, refine ACL policies, or integrate with cloud security solutions.**


