import os
from functions import *

penalty_messages = []
penalty_score = 0
report_messages = []
final_score = 0

def check(type, message, points, check1, check2, check3):
    global penalty_score
    global final_score
    if type == 'String_In_File':
        if String_In_File(check1, check2) == True:
            final_score = final_score + int(points)
            message = message + " - " + str(points) + " points."
            report_messages.append(message)
    if type == 'String_Not_In_File':
        if String_Not_In_File(check1, check2) == True:
            final_score = final_score + int(points)
            message = message + " - " + str(points) + " points."
            report_messages.append(message)
    if type == 'Package_Installed':
        if Package_Installed(check1) == True:
            final_score = final_score + int(points)
            message = message + " - " + str(points) + " points."
            report_messages.append(message)
    if type == 'Package_Not_Installed':
        if Package_Not_Installed(check1) == True:
            final_score = final_score + int(points)
            message = message + " - " + str(points) + " points."
            report_messages.append(message)
    if type == 'Firewall_Up':
        if Firewall_Up() == True:
            final_score = final_score + int(points)
            message = message + " - " + str(points) + " points."
            report_messages.append(message)
    if type == 'File_Exists':
        if File_Exists(check1) == True:
            final_score = final_score + int(points)
            message = message + " - " + str(points) + " points."
            report_messages.append(message)
    if type == 'File_Not_Exists':
        if File_Not_Exists(check1) == True:
            final_score = final_score + int(points)
            message = message + " - " + str(points) + " points."
            report_messages.append(message)
    if type == 'Directory_Exists':
        if Directory_Exists(check1) == True:
            final_score = final_score + int(points)
            message = message + " - " + str(points) + " points."
            report_messages.append(message)
    if type == 'Directory_Not_Exists':
        if Directory_Not_Exists(check1) == True:
            final_score = final_score + int(points)
            message = message + " - " + str(points) + " points."
            report_messages.append(message)
    if type == 'Directory_Not_Exists':
        if Directory_Not_Exists(check1) == True:
            final_score = final_score + int(points)
            message = message + " - " + str(points) + " points."
            report_messages.append(message)
    if type == 'User_Exists':
        if User_Exists(check1) == True:
            final_score = final_score + int(points)
            message = message + " - " + str(points) + " points."
            report_messages.append(message)
    if type == 'User_Not_Exists':
        if User_Not_Exists(check1) == True:
            final_score = final_score + int(points)
            message = message + " - " + str(points) + " points."
            report_messages.append(message)
    if type == 'Group_Exists':
        if Group_Exists(check1) == True:
            final_score = final_score + int(points)
            message = message + " - " + str(points) + " points."
            report_messages.append(message)
    if type == 'Group_Not_Exists':
        if Group_Not_Exists(check1) == True:
            final_score = final_score + int(points)
            message = message + " - " + str(points) + " points."
            report_messages.append(message)
    if type == 'User_In_A_Group':
        if User_In_A_Group(check1, check2) == True:
            final_score = final_score + int(points)
            message = message + " - " + str(points) + " points."
            report_messages.append(message)
    if type == 'User_Not_In_A_Group':
        if User_Not_In_A_Group(check1, check2) == True:
            final_score = final_score + int(points)
            message = message + " - " + str(points) + " points."
            report_messages.append(message)
    if type == 'Service_Is_Up':
        if Service_Is_Up(check1) == True:
            final_score = final_score + int(points)
            message = message + " - " + str(points) + " points."
            report_messages.append(message)
    if type == 'Service_Is_Not_Up':
        if Service_Is_Not_Up(check1) == True:
            final_score = final_score + int(points)
            message = message + " - " + str(points) + " points."
            report_messages.append(message)
    return True