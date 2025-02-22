#!/bin/bash

# Allow only hospital internal network
sudo ufw allow from 192.168.1.0/24 to any port 443

# Block all external SSH access
sudo ufw deny from 0.0.0.0/0 to any port 22

# Enable firewall
sudo ufw enable

echo "✅ Firewall rules applied successfully."
