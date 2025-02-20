import subprocess

def setup_ip_whitelist():
    subprocess.run(["ufw", "allow", "from", "192.168.1.100", "to", "any", "port", "80"])

if __name__ == '__main__':
    setup_ip_whitelist()

