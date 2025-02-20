import os

def setup_host_firewall():
    os.system("ufw allow from 192.168.1.0/24 to any port 22")
    os.system("ufw enable")

if __name__ == '__main__':
    setup_host_firewall()

