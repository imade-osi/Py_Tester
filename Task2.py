
"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
import os

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

max_time = None
max_num = ''
numbers_hash = {}

for call in calls:
    caller = call[0]
    receiver = call[1]
    length = int(call[3])

 
    if (caller in numbers_hash) & (receiver in numbers_hash):
        numbers_hash[caller] += length 
        numbers_hash[receiver] += length
    elif caller in numbers_hash:
        numbers_hash[caller] += length
        numbers_hash[receiver] = length
    elif receiver in numbers_hash:
        numbers_hash[receiver] += length
        numbers_hash[caller] = length
    else: 
        numbers_hash[caller] = length
        numbers_hash[receiver] = length

    if numbers_hash[caller] > max_time:
        max_time = numbers_hash[caller]
        max_num = call[0]
    elif numbers_hash[receiver] > max_time:
        max_time = numbers_hash[receiver]
        max_num = call[1]

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

os.system('clear')
print('< ' +max_num+ '> spent the longest time, <' +str(max_time)+ '> seconds, on the phone during') 

# <(080)33251027 > spent the longest time, < 90456 > seconds, on the phone during


# The Time complexity of this code adheres to O(n) since this code only iterates 
# the overall list of calls once. there are indeed several checks that are done at each pass 
# but they are a fixed number of comparison and hash insertions which operate on a constant time
# and will not increase depending on the size of the call list.  
