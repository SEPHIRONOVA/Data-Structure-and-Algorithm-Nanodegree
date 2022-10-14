"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
# Dictionary to store the total length for each caller
call_length = {}

for call in calls:
       if call[0] not in call_length.keys():
              call_length[call[0]] = int(call[3])
       else:
              call_length[call[0]] += int(call[3])
              
       if call[1] not in call_length.keys():
              call_length[call[1]] = int(call[3])
       else:
              call_length[call[1]] += int(call[3])

max_call_number = max(call_length, key = call_length.get)
max_call_length = max(call_length.values())

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(max_call_number, max_call_length))

# Worst Case Scenario
# Time Complexity O(n): Each record will at most 4 operations, 4n + 4(1 dict creation + 2 calculation + 1 print) => O(n)
# Space Complexity O(n): Store all records if all are distinct
