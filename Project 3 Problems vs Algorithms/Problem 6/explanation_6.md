## Explanation_6: Unsorted Integer Array

_Explanation:_
As we want to solve it in a single transversal, our method keeps two place holder for max and min. No specific data structure is needed. 
It starts with assume min and max value are the first and last element respectively, and compare all element with current min and max.

_Time Complexity:_
O(n) For each element in list, it compares to both min and max value. O(2n) => O(n)

_Space Complexity:_
O(1) It is constant as it uses fixed space for max, min, temp