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

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# number only call but not receive calls
call_number = []
receive_number = []

for call in calls:
    if call[0] not in call_number:
           call_number.append(call[0])
    if call[1] not in receive_number:
           receive_number.append(call[1])

# all text phone number
text_number = []

for text in texts:
    if text[0] not in text_number:
           text_number.append(text[0])
    if text[1] not in text_number:
           text_number.append(text[1])

possible_telemarketer = set(call_number) - set(receive_number) - set(text_number)

print("These numbers could be telemarketers: ")
for number in sorted(possible_telemarketer):
       print(number)

# Worst Case Scenario
# Time Complexity O(nlogn): For each call/text, at most 4 operations will be performed, so total 4n + n(print each number) + nlogn(sort) + 5(3 variable creations + print + set operation) => O(nlogn)
# Space Complexity O(n): Need to store number in both text/call if all are distinct 
