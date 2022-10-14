## Explanation_3: Rearrange Array Elements

_Explanation:_
As Python buildt-in function are inhibited, mergesort is tested first as it requires nlog(n) time complexity. It needs some modifiction as there is recursion and temporary recursion result is saved.
List is used as data structure to keep it easily accessible through indexing. 

_Time Complexity:_
O(nlog(n)) as mergesort is used here. Each time we compare an array we have approximate log(n) iterations. Multiply it by array number n. Plus two for loop together(n). So total is O(nlog(n)) + O(n) = O(nlog(n))

_Space Complexity:_
O(n) the space complexity is n as it require space with length of array for temporary storage