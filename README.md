# horusSE

A lightweight vulnerability remedition engine developed by Akshay Rohatgi.

Created to advance my own python skills and learn how to use python with linux. I am very interested in cybersecurity both offensive and defensive and this is where the idea for this project came from.

# Supported Functions
- String in file or string not in file
- Package is installed or not installed
- Firewall active
- File exists or does not exist
- Directory exists or does not exist
- User exists or does not exist
- Group exists or does not exist
- User is in a group or not in a group
- Service is up or down
- Permissions is or is not equal to something

# Documentation

## __Scoring__
- everything will be entered into the scoring function in scoring.py
```python
def scoring():
    penalty('Service_Is_Not_Up', 'Cron service has been stopped', -2, 'cron', None, None)
    penalty('File_Not_Exists', 'Important File Removed', -2, '/home/akshay/Desktop/check.txt', None, None)

    check('String_In_File', 'Line in file found', 3, '/home/akshay/Desktop/check.txt', 'hello', None)
    check('File_Permissions_Is', '/etc/passwd has secure permissions', 5, '/etc/passwd', 644, None)
    check('Package_Installed', 'Required Package installed', 2, 'yelp', 'None', None)
    check('User_Not_Exists', 'Unauthorized user removed', 1, 'checkuser', None, None)
    check('User_Exists', 'User added', 3, 'user2', None, None)
```
- Checks have a maximum of 3 arguments, some checks have less than 3 so the checks with less than 3 will have None in the check place.

- Checks structure works like this:
```
check( or penalty( specifies if it will be scored as a penalty or a scoring check

check(
```

- the first argument to either of those functions will be something like this:
```
specifies type of check/penalty

check('String_In_File'
```

- The second argument is the message displayed on the score report if the check passes
```
specifies message

check('String_In_File', 'Line in file found
```

- The third argument is point value given if the check passes
```
specifies point value
check('String_In_File', 'Line in file found', 3
```

- The rest of the arguments vary on the type of check, here are some examples:
```
check('String_In_File', 'Line in file found', 4, '/etc/hello.txt', 'hello', None)

check('File_Not_Exists', 'Prohibited file removed', 3, '/etc/medusa.zip', None, None)

check('User_Exists', 'User root exists', 2, 'root', None, None)

check('Firewall_Up', 'Firewall is enabled', 1, None, None, None)
```

- These can all be penalties as well
```
penalty('Service_Is_Not_Up', 'Cron service has been stopped', -2, 'cron', None, None)

penalty('File_Not_Exists', 'Important File Removed', -2, '/etc/hello.txt', None, None)

```

- For setup just clone the repo with
```
$ cd /opt/
$ git clone https://github.com/Akshay-Rohatgi/horusSE

$ sudo bash install.sh
```
- configure your vulns and then run the release script 
```$ sudo bash release.sh```

# Checks:
- all of these checks can be used as penalties as well by just using the penalty() function

__String_In_File__/__String_Not_In_File__ - checks to see if a string exists or does not exist in a file
```
check('String_In_File', 'Line in file found', 3, '/home/akshay/Desktop/check.txt', 'hello', None)

check('String_Not_In_File', 'Line in file not found', 3, '/home/akshay/Desktop/check.txt', 'hackerman hacks', None)
```

__Package_Installed__/__Package_Not_Installed__ - checks to see if a string exists or does not exist in a file
```
check('Package_Installed', 'Required Package installed', 2, 'yelp', 'None', None)

check('Package_Not_Installed', 'Prohibited Package removed', 2, 'nmap', 'None', None)
```

__Firewall_up__ - checks if the firewall is up or not
```
check('Firewall_Up', 'Firewall is enabled', 1, None, None, None)
```

__File_Exists__/__File_Not_Exists__ - checks to see if the file exists or not
```
check('File_Exists', 'Required File added', 3, '/home/checkuser/notes.txt', None, None)

check('File_Not_Exists', 'Prohibited file removed', 3, '/etc/medusa.zip', None, None)
```

__Directory_Exists__/__Directory_Not_Exists__ - checks to see if the directory exists or not
```
check('Directory_Exists', 'Required Directory added', 3, '/home/checkuser/notes', None, None)

check('Directory_Not_Exists', 'Prohibited Directory removed', 3, '/etc/hackingnotes', None, None)
```

__User_Exists__/__User_Not_Exists__ - checks to see if the user exists or not
```
check('User_Exists', 'User root exists', 2, 'root', None, None)

check('User_Not_Exists', 'Prohibited user account removed', 2, 'hackerman', None, None)
```

__Group_Exists__/__Group_Not_Exists__ - checks to see if the user exists or not
```
check('Group_Exists', 'admins group exists', 2, 'adm', None, None)

check('Group_Not_Exists', 'Prohibited group removed', 2, 'hackers', None, None)
```

__Service_Is_Up__/__Service_Is_Not_Up__ - checks to see if the user exists or not
```
check('Service_Is_Up', 'cron service is up', 2, 'cron', None, None)

check('Service_Is_Not_Up', 'Prohibited service is removed or stopped', 2, 'nfs', None, None)
```

__File_Permissions_Is__/__File_Permissions_Is_Not__ - checks to see if the user exists or not
```
check('File_Permissions_Is', '/etc/passwd has secure permissions', 5, '/etc/passwd', 644, None)

check('File_Permissions_Is_Not', '/etc/group is not world writable', 5, '/etc/group', 777, None)
```


# TODO:
- maybe a way to compile so cheating couldnt exist? pyc?
- regex checks
