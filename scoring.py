from vuln_load import check, report_messages, penalty_messages, check_scores, penalty_scores, penalty, possible_scores, vulncount


# ADD YOUR VULNS HERE
def scoring():
    penalty('String_Not_In_File', 'check 2 passed', -3, '/home/akshay/Desktop/check.txt', 'green', None)
    penalty('String_Not_In_File', 'check 2 passed', -3, '/home/akshay/Desktop/check.txt', 'green', None)

    check('String_In_File', 'check 1 passed', 8, '/home/akshay/Desktop/check.txt', 'hello', None)
    check('String_In_File', 'check 1 passed', 8, '/home/akshay/Desktop/check.txt', 'hello', None)
    check('String_In_File', 'check 1 passed', 8, '/home/akshay/Desktop/check.txt', 'hello', None)
    check('String_In_File', 'check 1 passed', 2, '/home/akshay/Desktop/check.txt', 'green', None)


scoring()

# Important variables
possible_vulncount = sum(vulncount)
possible_sum = sum(possible_scores)
check_sum = sum(check_scores)
penalty_sum = sum(penalty_scores)

current_vulncount = len(check_scores)
finalscore = check_sum + penalty_sum

message_One = str(current_vulncount) + " out of " + str(possible_vulncount) + " scored security issues fixed, for a gain of " + str(finalscore) + " points:"
message_Two = str(finalscore) + " points out of " + str(possible_sum) + " points recieved"
