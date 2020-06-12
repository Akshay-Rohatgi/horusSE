import os
import subprocess
import os.path
from os import path
import re

def String_In_File(path, string):
    with open(path, 'r') as handle:
        for line in handle:
            if string in line:
                return True
    return False

def String_Not_In_File(path, string):
    with open(path, 'r') as handle:
        for line in handle:
            if string in line:
                return False
    return True

def Package_Installed(package):
    handle = subprocess.getoutput("dpkg --get-selections | awk '{print $1}'")
    if package in handle:
        return True
    return False

def Package_Not_Installed(package):
    handle = subprocess.getoutput("dpkg --get-selections | awk '{print $1}'")
    if package in handle:
        return False
    return True

def Firewall_Up():
    handle = subprocess.getoutput("sudo ufw status | grep 'Status: active'")
    if handle == 'Status: active':
        return True
    else:
        return False

def File_Exists(path):
    if os.path.exists(path):
        return True
    return False

def File_Not_Exists(path):
    if os.path.exists(path):
        return False
    return True

def Directory_Exists(path):
    if os.path.exists(path):
        return True
    return False

def Directory_Not_Exists(path):
    if os.path.exists(path):
        return False
    return True

def User_Exists(username):
    handle = subprocess.getoutput("cut -d: -f1 /etc/passwd")
    if username in handle:
        return True
    return False

def User_Not_Exists(username):
    handle = subprocess.getoutput("cut -d: -f1 /etc/passwd")
    if username in handle:
        return False
    return True

def Group_Exists(group):
    handle = subprocess.getoutput("cut -d: -f1 /etc/group")
    if group in handle:
        return True
    return False

def Group_Not_Exists(group):
    handle = subprocess.getoutput("cut -d: -f1 /etc/group")
    if group in handle:
        return False
    return True

def User_In_A_Group(username, group):
    handle = subprocess.getoutput("groups '" + username + "' | grep '" + group + "'")
    if username in handle:
        return True
    return False

def User_Not_In_A_Group(username, group):
    handle = subprocess.getoutput("groups '" + username + "' | grep '" + group + "'")
    if username in handle:
        return False
    return True

def Service_Is_Up(service):
    handle = subprocess.getoutput("systemctl is-active '" + service + "'")
    if handle == 'active':
        return True
    return False

def Service_Is_Not_Up(service):
    handle = subprocess.getoutput("systemctl is-active '" + service + "'")
    if handle == 'inactive':
        return True
    return False
