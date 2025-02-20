import os

def setup_acl_permissions():
    os.system("setfacl -m u:username:rwx /path/to/directory")

if __name__ == '__main__':
    setup_acl_permissions()

