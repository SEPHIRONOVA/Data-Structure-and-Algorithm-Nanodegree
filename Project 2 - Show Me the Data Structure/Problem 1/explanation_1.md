## Explanation_1: LRU Cache

_Data Structure:_

- 'Double Linked List': It offers constant time to add/remove a node
- 'Hashtable': It uses constant time to search

_Time Complexity:_
The time complexity is O(1). It offers a combination of 'Hashtable' and 'Double Linked List'. All operations have constant time 'O(1)'

_Space Complexity:_

- Dictionary Space: 'O(n)'
- Double Linked List Space: 'O(n)'
- Cursor Space(Temporary): 'O(1)'

Total Space Complexity = 'O(n + n + 1)' = 'O(n)'
