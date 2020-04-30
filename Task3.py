"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import os

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


def Bangalore_check(num):
  if (num[0] == '(') & (num[1] == '0') & (num[2] == '8') & (num[3] == '0') & (num[4] == ')'):
    return True


def Tele_check(num):
  if (num[0] == '(') & (num[1] == '1') & (num[2] == '4') & (num[3] == '0') & (num[4] == ')'):
    return True


# mobile_prefix = first 4, ' ' in middle
# fixed_line_prefix = between (), random length
# telemarketers_prefix = first 3, start with 140
# all called from bangalore prefix = (080)

call_hash = {}
bang_count = 0
total_count = 0

for call in calls:
  
  if Bangalore_check(call[0]):
    if Bangalore_check(call[1]):

      bang_count += 1
      total_count += 1

      call[1]
      num = call[1][1]+call[1][2]+call[1][3]
      call_hash[num] = True

    elif call[1][6] == ' ':
      total_count += 1
      num = call[1][1]+call[1][2]+call[1][3]+call[1][4]+call[1][5]
      call_hash[num] = True
    elif Tele_check(call[1]):
      total_count += 1
      num = call[1][1]+call[1][2]+call[1][3]
      call_hash[num] = True
    elif call[1][6] == ')':
      total_count += 1
      num = call[1][1]+call[1][2]+call[1][3]+call[1][4]+call[1][5]
      call_hash[num] = True
    elif call[1][5] == ')':
      total_count += 1
      num = call[1][1]+call[1][2]+call[1][3]+call[1][4]
      call_hash[num] = True
    else:
      total_count += 1
      num = call[1][1]+call[1][2]+call[1][3]
      call_hash[num] = True



os.system('clear')

print("\nThe numbers called by people in Bangalore have codes:\n ")
for key in sorted(call_hash):
    print(key)

percentage = round((int(bang_count) * 1.0) / (int(total_count)),3)
print(bang_count)
print(total_count)
print('\n < ' + str(percentage) +'% > percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.')

# The numbers called by people in Bangalore have codes:

# 008
# 019
# 022
# 035
# 036
# 040
# 04344
# 044
# 04546
# 0471
# 080
# 0821
# 151
# 152
# 241
# 242
# 301
# 341
# 342
# 343
# 400
# 406
# 431
# 448
# 449
# 526
# 656
# 714
# 738
# 740
# 741
# 742
# 795
# 813
# 829
# 844
# 845
# 900
# 961
# 268
# 1080
# < 0.248 % > percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.
"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
