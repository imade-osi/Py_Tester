import os

"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    # print(texts)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""


first_inc_num = texts[0][0]
first_ans_num = texts[0][1]
first_call_time = texts[0][2]

last_inc_num = calls[-1][0]
last_ans_num = calls[-1][1]
last_call_time = calls[-1][2]
last_call_sec = calls[-1][3]

os.system('clear')
print('First record of texts, <' +first_inc_num+ '> texts, <' +first_ans_num+ '> at time, <' +first_call_time+ '>')
print('Last record of calls, <' +last_inc_num+ '> calls, <' +last_ans_num+ '> at time, <' +last_call_time+ '> lasting, <' +last_call_sec+ '> seconds')

# First record of texts, < 97424 22395 > texts, < 90365 06212 > at time, < 01-09-2016 06: 03: 22 >
# Last record of calls, < 98447 62998 > calls, < (080)46304537 > at time, < 30-09-2016 23: 57: 15 > lasting, < 2151 >
# seconds


# The Time complexity of this code adheres to O(1) since this code only onvoked 
# several array value look ups which is constant time in 
# an array with a given index
