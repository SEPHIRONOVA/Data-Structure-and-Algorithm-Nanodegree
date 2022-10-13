## Explanation_5: Autocomplete with Trie

_Explanation:_
is_word is used to check if any word is inserted as a child(children)
Children uses hashmap to quickly access the char in the children

_Time Complexity:_
1. Insert:
O(l_max) for worst case as it need to check if the current char is in the children.

2. suffixes:
O(n * l_max) is the approximate time complexity. In the equation, n is number of words and l_max is the length of longest word 

_Space Complexity:_
1. insert:
O(l_max) for worst case as it need a Trie to store each char.

2. suffixes:
O(c**(l_max+1)) where c is the total number of char type used for and l_max is the length longest word. It requires this space to store all words.