from vuln_load import check, report_messages, penalty_messages, check_scores, penalty_scores, penalty

def scoring():
    penalty('String_Not_In_File', 'check 2 passed', -3, '/home/akshay/Desktop/check.txt', 'green', None)
    penalty('String_Not_In_File', 'check 2 passed', -3, '/home/akshay/Desktop/check.txt', 'green', None)

    check('String_In_File', 'check 1 passed', 8, '/home/akshay/Desktop/check.txt', 'hello', None)
    check('String_In_File', 'check 1 passed', 8, '/home/akshay/Desktop/check.txt', 'hello', None)
    check('String_In_File', 'check 1 passed', 8, '/home/akshay/Desktop/check.txt', 'hello', None)

scoring()
checksum = sum(check_scores)
penaltysum = sum(penalty_scores)
finalscore = checksum + penaltysum
print(checksum)
print(check_scores)
print(penalty_scores)
print(report_messages)
print(penalty_messages)
print(finalscore)