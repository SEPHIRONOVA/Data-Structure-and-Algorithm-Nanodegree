## Explanation_7: HTTPRouter using a Trie

_Explanation:_
A Trie is used to complete HTTPRouter separated by "/". 

_Time Complexity:_
### 1. Creating a Trie
O(nm) where n is longest path separated by m "/" and m is total number of keys for each/one of the path.

### 2. Searching
O(n) Searching depend on the length of the path separated by "/"

### 3. Inserting
O(n) Similarly, inserting depend on the length of the path separated by "/"

_Space Complexity:_
O(n) It is determined by the number of components separated by "/"