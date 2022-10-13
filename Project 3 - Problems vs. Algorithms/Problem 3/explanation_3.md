## Explanation_3: Rearrange Array Elements

_Explanation:_
Mergesort is used here as it requires nlog(n) time complexity. 

_Time Complexity:_
O(nlog(n)) as mergesort is used here. Each time we compare an array we have approximate log(n) iterations. Multiply it by array number n. Plus two for loop together(n). So total is O(nlog(n)) + O(n) = O(nlog(n))

_Space Complexity:_
O(n) the space complexity is n as it require space with length of array for temporary storage