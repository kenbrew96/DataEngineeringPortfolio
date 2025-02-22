import os

def apply_whitelist():
    os.system("sudo ufw allow from 203.0.113.0/24")
    os.system("sudo ufw enable")
    print("✅ Whitelist rules applied successfully.")

if __name__ == "__main__":
    apply_whitelist()
