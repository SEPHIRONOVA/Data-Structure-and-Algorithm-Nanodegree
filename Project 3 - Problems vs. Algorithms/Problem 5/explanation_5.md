## Explanation_5: Autocomplete with Trie

_Explanation:_
Trie sturcture is used for this problem as requirement and it serve the purpose well for easy insertion and search. is_word is used to check if any word is inserted as a child(children)
Children uses hashmap to quickly access the char in the children.

_Time Complexity:_
### class Trie
#### 1. __init__
O(1) as it takes constant time to create an empty TrieNode

#### 2. insert
O(n) as it needs to go through all existing words at worst case. l_max is the length of longest word 

#### 3. find
O(n * m) where m is the length of word and n is the number of char(children) available in one level. At worst case, it need to trasverse all possible words

### class TrieNode
#### 1. __init__
O(1) it only initialize the children and an indicator

#### 2. Insert:
O(n) for worst case as it need to check if the current char is in the children.

#### 3. suffixes:
O(n * m) is the approximate time complexity. In the equation, n is number of words and m is the length of the word. 
Essentially, n * m equals total number of words if none of them have common components. 

_Space Complexity:_
### class Trie
#### 1. __init__
O(1) as it only create an empty TreNode as root

#### 2. trie storage 
O(n * m) where m is the length of word and n is the number of char(children) available in one level

#### 3. insert
O(n) as it needs to loop through all existing children for temporary storage at worst case with no overlap. n is number of words

#### 4. find
O(n) where n is the word length when no common char at all.

### class TrieNode
#### 1. __init__
O(1) as it create an empty dictionary to store its children with a is_word indicator

#### 2. trie storage 
O(n * m) where n is the length of word and m is the number of char(children) available in one level

#### 3. insert:
O(n) for worst case as it need a Trie to store every single char.

#### 4. suffixes:
O(n * m) It is similar to storage when we do suffixes as it recursively go through all the possible words