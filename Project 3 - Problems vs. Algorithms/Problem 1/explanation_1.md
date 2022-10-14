## Explanation_1: Square Root of an Integer

_Explanation:_
Binary search is used as the time complexity requirement is O(log(n)). It is impossible to loop through 1 to n to find the number. 
Given the choice in the algo, divide the number into parts will satisfy the requirement. No specific data structure required.

_Time Complexity:_
O(log(n)) Each time divide the value by 2 and try to find the closer half

_Space Complexity:_
O(1) the space complexity is constant