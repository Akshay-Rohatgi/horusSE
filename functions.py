import os
import subprocess

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