## Explanation_6: Unsorted Integer Array

_Explanation:_
Assume min and max value are the first and last element respectively, and compare all element with current min and max.

_Time Complexity:_
O(n) For each element in list, it compares to both min and max value. O(2n) => O(n)

_Space Complexity:_
O(1) It is constant as it uses fixed space for max, min, temp