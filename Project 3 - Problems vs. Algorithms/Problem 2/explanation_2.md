## Explanation_2: Search in a Rotated Sorted Array 

_Explanation:_
Binary search will give us log(n) complexity. The worst case for loop through it's still O(n) which not satisfy the requirement. 
A recursive binary search is used as the search process is similar across each section. List is used for quickly accessible by index.

_Time Complexity:_
O(log(n)) as binary search is used here. The time complexity depends on the recursive depth of the array(related to length of array)

_Space Complexity:_
O(log(n)) It need to store temporary data on either left/right part of array. So approximately the space required is O(log(n)).