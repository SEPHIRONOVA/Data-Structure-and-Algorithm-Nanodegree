## Explanation_2: Search in a Rotated Sorted Array 

_Explanation:_
The worst case for loop through it's still O(n) which not satisfy the requirement. Binary search will give us log(n) complexity. A recursive binary search is used as the search process is similar across each section.

_Time Complexity:_
O(log(n)) as binary search is used here. The time complexity depends on the recursive depth of the array(related to length of array)

_Space Complexity:_
O(1) the space complexity is constant