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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
text_1 = texts[0]
print("First record of texts, {} text {} at time {}".format(text_1[0], text_1[1], text_1[2]))

call_last = calls[-1]
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(call_last[0], call_last[1], call_last[2], call_last[3]))

# Worst Case Scenario
# Time Complexity O(1) => constant 
# Space Complexity O(1) => constant