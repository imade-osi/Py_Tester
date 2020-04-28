import os

"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

#hash to keep track of all numbers as keys
call_hash = {}

for call in calls:

    #Use of hash just in case there are duplicate numbers in calls list
    call_hash[call[0]] = True
    call_hash[call[1]] = True 

numbers = len(call_hash)
caller = len(calls)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

os.system('clear')
print('There are <' +str(numbers)+ '> different telephone numbers in the records.')
print(caller)

# There are < 551 > different telephone numbers in the records.
# 5213


# The Time complexity of this code adheres to O(n) since this code iterates trhough 
# the calls list once and uses constant time  insertion of hashes in order to 
# fill call_hash with key value pairs. There are two additiotional linear 
# checks to acheive the length but the number of times these checks are callses
# stays constant even if the size of list were change
