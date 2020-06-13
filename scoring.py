from vuln_load import check, report_messages, penalty_messages, check_scores, penalty_scores, penalty, possible_scores, vulncount, penaltycount, possible_penalties
from datetime import datetime
import os
import subprocess

# ADD YOUR VULNS HERE
def scoring():
    penalty('Service_Is_Not_Up', 'Cron service has been stopped', -2, 'cron', None, None)
    penalty('File_Not_Exists', 'Important File Removed', -2, '/home/akshay/Desktop/check.txt', None, None)

    check('String_In_File', 'Line in file found', 3, '/home/akshay/Desktop/check.txt', 'hello', None)
    check('File_Permissions_Is', '/etc/passwd has secure permissions', 5, '/etc/passwd', 644, None)
    check('Package_Installed', 'Required Package installed', 2, 'yelp', 'None', None)
    check('User_Not_Exists', 'Unauthorized user removed', 1, 'checkuser', None, None)
    check('User_Exists', 'User added', 3, 'user2', None, None)

scoring()

def gain():
  os.system("notify-send 'You gained points!'")
  os.system("aplay web/gain.wav > /dev/null 2>&1")
  print('You gained points!')

def lose():
  os.system("notify-send 'You lost points!'")
  os.system("aplay web/alarm.wav > /dev/null 2>&1")
  print('You lost points!')

# Important variables
now = datetime.now()
possible_vulncount = sum(vulncount)
possible_sum = sum(possible_scores)
check_sum = sum(check_scores)
penalty_sum = sum(penalty_scores)

current_penaltycount = len(penalty_scores)
current_vulncount = len(check_scores)

c = open('oldscore.txt', 'r')
oldscore = c.readline()

finalscore = check_sum + penalty_sum

if str(finalscore) > oldscore:
  gain()
elif str(finalscore) < oldscore:
  lose()

g = open('oldscore.txt', 'w')
g.write(str(finalscore))
g.close()

message_One = str(current_vulncount) + " out of " + str(possible_vulncount) + " scored security issues fixed, for a gain of " + str(finalscore) + " points:"
message_Two = str(finalscore) + " points out of " + str(possible_sum) + " points recieved"

def report_write():
    f = open('web/score_report.html', 'w')
    base = """<!DOCTYPE HTML>
<html>

<head>
  <link rel="icon" type="image/png" href="best.png">
  <title>horusSE Scoring Report</title>
  <style type="text/css">
    h1 {
      text-align: center;
    }

    h2 {
      text-align: center;
    }

    body {
      font-family: Arial, Verdana, sans-serif;
      font-size: 14px;
      margin: 0;
      padding: 0;
      width: 100%;
      height: 100%;
      background-color: white;
    }

    .red {
      color: red;
    }

    .green {
      color: green;
    }

    .blue {
      color: blue;
    }

    .main {
      margin-top: 10px;
      margin-bottom: 10px;
      margin-left: auto;
      margin-right: auto;
      padding: 0px;
      background-color: white;
      width: 900px;
      max-width: 100%;
      min-width: 600px;
      box-shadow: 0px 0px 12px red;
    }

    .text {
      padding: 12px;
      color: grey;
    }

    .center {
      text-align: center;
    }
  </style>
</head>

<body>
  <div class="main">
    <div class="text">
      <p align=center style="width:100%;text-align:center"><IMG align=middle style="float:middle" src="best.png"
          alt="Image" height="150" width="150"></p>


      <h1> Score Report </h1>
      """
    
    time = "<h2>Report Generated On: " + str(now) + "</h2>"
    other ="""
      <h3 class="center">Current Team ID: <span style="color:red"> student </span></h3>"""
      
    count = """<h2>""" + message_Two + "</h2>"

    possible = """<P>
      <h3>""" + message_One + """</h3>"""

    more ="""
      <br>Users check passed - <span style="color:red">2 points</span>
      <br>Users check passed - <span style="color:red">2 points</span>
      <br>Users check passed - <span style="color:red">3 points</span>
      <br>Local Policy check passed <span style="color:red">3 points</span>"""

    more = """</div>
  </div>
</body>"""

    footer = """<FOOTER>
  <span style="font-size:11px">
    <center>
      <br>horusSE Linux Report
      <br>Developed by Akshay Rohatgi.
      <br>This is NOT an official Air Force Association (AFA) CyberPatriot Image; The AFA was not involved in the
      creation of, and does not endorse, this image.
  </span>
  </center>
</FOOTER>

</HTML>
"""
    f.write(base)
    f.write(time)
    for penalty in penalty_messages:
      add = """<h2><span style="color:red; font-size: large; font-weight: 1000; text-align: center;">Penalty: """ + penalty + """</span></h2>"""
      f.write(add)
    f.write(other)
    f.write(count)
    f.write(possible)
    for message in report_messages:
        insert = """<br>""" + message + """</span>"""
        f.write(insert)
    f.write(more)
    f.write(footer)
    f.close()
    return True

report_write()
os.system('cat web/logo.txt')