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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
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
called_by_bangalore = {}

def find_prefixes(phone_number):
       if phone_number[:5] == '(080)':
              return '(080)'
       elif (phone_number[0] in ['7','8','9']) & (phone_number[5] == ' '):
              return phone_number[:4]
       elif phone_number[:3] == '140':
              return '140'
       else:
              right_bracket_index = phone_number.index(")")
              return phone_number[:right_bracket_index+1]

# Part A
for call in calls:
       temp_call_prefix = find_prefixes(call[0]) # Prefix for calling from number
       temp_receive_prefix = find_prefixes(call[1]) # Prefix for call receiver number
       
       if (temp_receive_prefix not in called_by_bangalore.keys()):
              if temp_call_prefix == '(080)':
                     called_by_bangalore[temp_receive_prefix] = 1     
       else: 
              if temp_call_prefix == '(080)':
                     called_by_bangalore[temp_receive_prefix] += 1

print("The numbers called by people in Bangalore have codes:")
for key in sorted(called_by_bangalore.keys()):
       print(key)

# Part B
from_bangalore = sum(list(called_by_bangalore.values()))
to_bangalore_fixed = called_by_bangalore['(080)']

percentage = (to_bangalore_fixed / from_bangalore) * 100.00

print("\n{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentage))

# Worst Case Scenario
# Time Complexity O(n*n): For each call, at most opeartions(5 from each function call * 2 + n(check from conditional statement) + 2) executed,
# so total n * n + nlogn(sort) + constant => O(n*n)
# Space Complexity O(n): Need to store number of possible call prefix if all are distinct
