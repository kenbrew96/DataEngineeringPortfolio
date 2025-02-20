import subprocess

def setup_software_whitelist():
    subprocess.run(["ufw", "allow", "from", "192.168.1.100", "to", "any", "port", "22"])

if __name__ == '__main__':
    setup_software_whitelist()

