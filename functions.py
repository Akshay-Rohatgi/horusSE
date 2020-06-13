import os
import subprocess
import os.path
from os import path
import re

def String_In_File(path, string):
    try:
        with open(path, 'r') as handle:
            for line in handle:
                if string in line:
                    return True
    except: return False

def String_Not_In_File(path, string):
    try:
        with open(path, 'r') as handle:
            for line in handle:
                if string in line:
                    return False
    except: return True

def Package_Installed(package):
    try: 
        handle = subprocess.getoutput("dpkg --get-selections | awk '{print $1}'")
        if package in handle:
            return True
    except: return False

def Package_Not_Installed(package):
    try:
        handle = subprocess.getoutput("dpkg --get-selections | awk '{print $1}'")
        if package in handle:
            return False
    except: return True

def Firewall_Up():
    try:
        handle = subprocess.getoutput("sudo ufw status | grep 'Status: active'")
        if handle == 'Status: active':
            return True
        else:
            return False
    except: return False

def File_Exists(path):
    try:
        if os.path.exists(path):
            return True
    except: return False

def File_Not_Exists(path):
    try:
        if os.path.exists(path):
            return False
    except: return True

def Directory_Exists(path):
    try:
        if os.path.exists(path):
            return True
    except: return False

def Directory_Not_Exists(path):
    try:
        if os.path.exists(path):
            return False
    except: return True

def User_Exists(username):
    try:
        handle = subprocess.getoutput("cut -d: -f1 /etc/passwd")
        if username in handle:
            return True
    except: return False

def User_Not_Exists(username):
    try:
        handle = subprocess.getoutput("cut -d: -f1 /etc/passwd")
        if username in handle:
            return False
    except: return True

def Group_Exists(group):
    try:
        handle = subprocess.getoutput("cut -d: -f1 /etc/group")
        if group in handle:
            return True
    except: return False

def Group_Not_Exists(group):
    try:
        handle = subprocess.getoutput("cut -d: -f1 /etc/group")
        if group in handle:
            return False
    except: return True

def User_In_A_Group(username, group):
    try:
        handle = subprocess.getoutput("groups '" + username + "' | grep '" + group + "'")
        if username in handle:
            return True
    except: return False

def User_Not_In_A_Group(username, group):
    try:
        handle = subprocess.getoutput("groups '" + username + "' | grep '" + group + "'")
        if username in handle:
            return False
    except: return True

def Service_Is_Up(service):
    try:
        handle = subprocess.getoutput("systemctl is-active '" + service + "'")
        if handle == 'active':
            return True
    except: return False

def Service_Is_Not_Up(service):
    try:
        handle = subprocess.getoutput("systemctl is-active '" + service + "'")
        if handle == 'inactive':
            return True
    except: return False

def File_Permissions_Is(path, value):
    try:
        handle = subprocess.getoutput("stat -c '%a' " + path)
        if int(value) == int(handle):
            return True
    except: return False

def File_Permissions_Is_Not(path, value):
    try:
        handle = subprocess.getoutput("stat -c '%a' " + path)
        if int(value) == int(handle):
            return False
    except: return True