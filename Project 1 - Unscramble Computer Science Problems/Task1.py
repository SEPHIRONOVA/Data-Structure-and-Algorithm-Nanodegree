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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
phone_number = set()

for text in texts:
    phone_number.add(text[0])
    phone_number.add(text[1])
           
for call in calls:
    phone_number.add(call[0])
    phone_number.add(call[1])
           
print("There are {} different telephone numbers in the records.".format(len(phone_number)))

# Worst Case Scenario
# Time Complexity O(n): Each record will at most 2 operations, 2n + 2(set + print) => O(n)
# Space Complexity O(n): Store all records if all are distinct
