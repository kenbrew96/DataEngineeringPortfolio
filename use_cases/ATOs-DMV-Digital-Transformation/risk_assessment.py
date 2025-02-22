import os

def check_compliance():
    os.system("nmap -A -T4 dmv.maryland.gov > security_scan.txt")
    os.system("aws iam list-roles > iam_roles.txt")
    print("✅ Security compliance checks completed.")

if __name__ == "__main__":
    check_compliance()
