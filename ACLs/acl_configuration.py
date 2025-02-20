import os

def configure_acl():
    os.system("setfacl -m g:groupname:rx /path/to/directory")

if __name__ == '__main__':
    configure_acl()

