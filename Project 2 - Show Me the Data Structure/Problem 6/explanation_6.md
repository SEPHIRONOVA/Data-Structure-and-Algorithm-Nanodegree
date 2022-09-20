## Explanation_6: Union and Intersection

_Data Structure:_

- 'LinkedList': LinkedList is used as the required data structure

_Time Complexity:_
append => O(n) as it iterate the whole LinkedList
get_size => O(n) as it iterate the whole LinkedList
to_list => O(n) as it iterate the whole LinkedList

union => O(nlog(n)) = O(n + n + O(nlog(n)) + n ) Note: append one by one take nlog(n) time but not n\*n
intersection => O(nlog(n)) = O(n + n + nlog(n))

_Space Complexity:_
O(n) where n is the sum of length of both LinkedList
