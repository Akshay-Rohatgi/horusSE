#!/bin/bash

echo "What is your username?"

read username
echo "setting up image with username $username"

chmod +x desktop/*
mv desktop/* /home/$username/Desktop/


echo "creating horus_score command..."
touch /usr/local/bin/horus_score

echo """#!/bin/bash
if [[ $USER != "root" ]]; then
   echo "You must be root to run this script!"
   exit 1
fi

python3 /opt/horusSE/scoring.py"""

sudo chmod +x /usr/local/bin/horus_score

echo "removing log files..."

chmod 755 -R /opt/horusSE
find / -name '.bash_history' -exec ln -sf /dev/null {} \\;
find / -name '.zsh_history' -exec ln -sf /dev/null {} \\;
rm -rf /root/.local /home/*/.local/
rm -rf /root/.cache /home/*/.cache/
find / -type f -iname '*.swp' -delete
rm -rf /root/*~ /home/*/Desktop/*~
rm -rf /var/log/apt/* /var/log/dpkg.log
rm -f /var/log/auth.log* /var/log/syslog
rm -f /var/log/installer/initial-status.gz
find /etc -exec  touch --date='2012-12-12 12:12' {} \\; 2>/dev/null
find /home -exec  touch --date='2012-12-12 12:12' {} \\; 2>/dev/null
find /var -exec  touch --date='2012-12-12 12:12' {} \\; 2>/dev/null
find /opt -exec  touch --date='2012-12-12 12:12' {} \\; 2>/dev/null

echo "done"