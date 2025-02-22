import os

def apply_acl():
    os.system("sudo setfacl -m u:faculty:rwx /library_resources")
    os.system("sudo setfacl -m u:student:r-- /library_resources")
    os.system("sudo setfacl -m u:guest:--- /library_resources")
    print("✅ ACL rules applied successfully.")

if __name__ == "__main__":
    apply_acl()
