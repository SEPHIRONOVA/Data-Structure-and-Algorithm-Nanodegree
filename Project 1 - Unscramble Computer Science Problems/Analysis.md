Task 0
Worst Case Scenario
Time Complexity O(1) => constant 
Space Complexity O(1) => constant

Task 1
Worst Case Scenario
Time Complexity O(n): Each record will at most 2 operations, 2n + 2(set + print) => O(n)
Space Complexity O(n): Store all records if all are distinct

Task 2
Worst Case Scenario
Time Complexity O(n): Each record will at most have 4 operations, 4n + 4(1 dict creation + 2 calculation + 1 print) => O(n)
Space Complexity O(n): Store all records if all are distinct

Task 3
Worst Case Scenario
Time Complexity O(n*n): For each call, at most opeartions(5 from each function call * 2 + n(check from conditional statement) + 2) executed, so total n * n + nlogn(sort) + constant => O(n*n)
Space Complexity O(n): Need to store number of possible call prefix if all are distinct

Task 4
Worst Case Scenario
Time Complexity O(nlogn): For each call/text, at most 4 operations will be performed, so total 4n + n(print each number) + nlogn(sort) + 5(3 variable creations + print + set operation) => O(nlogn)
Space Complexity O(n): Need to store number in both text/call if all are distinct 
