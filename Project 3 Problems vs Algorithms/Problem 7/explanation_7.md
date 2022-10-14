## Explanation_7: HTTPRouter using a Trie

_Explanation:_
A Trie is used to complete HTTPRouter separated by "/" as the required data structure. It can be easily implemented by a Tree Structure. 
The children is stored in a hashmap which implemented by dictionary for easy access.

_Time Complexity:_
### Class RouteTrie
#### 1. __init__
O(1) It takes constant time to add initialize a RouteTrieNode with handler 

#### 2. find
O(n) It depend on the numbre of components separated by "/" that need to be find.

#### 3. insert
O(n) Similarly, inserting depend on the length of the path separated by "/"

### Class RouteTrieNode
#### 1. __init__
O(1) it only initialize the handler and an indicator

#### 2. insert
O(1) It simply add the new path to its children

### Class Router
#### 1. __init__
O(1) It takes constant time to store both handlers and initialize a RouteTrie as shown above

#### 2. add_handler
O(n) It includes split_path and insert function in the Class RouteTrieNode. O(n + 1) = O(n)

#### 3. lookup
O(n * m) It include split_path, a for loop to iterates all children and few checks. O(n + nm + 1) = O(nm) where m is number of children need to be checked and n is number of component.
Essentially, worst case need to check all existing path available(if consider total is n) if there is not any common components among them.

#### 4. split_path
O(n) as it includes the split by number of "/" and other O(1) checks

_Space Complexity:_
### Class RouteTrie
#### 1. __init__
O(1) It takes constant space to initialize a RouteTrieNode as shown above 

#### 2. find
O(n) It depend on the number of components separated by "/" that need to be found.

#### 3. insert
O(n) Worst case non-common words will need to go through and create new place for each components

### Class RouteTrieNode
#### 1. __init__
O(1) it takes constance space to store handler and create an empty dictionary

#### 2. insert
O(n) It depend on the number of components separated by "/"

### Class Router
#### 1. __init__
O(1) It takes fixed amount of storage to create a empty RouteTrie and store the handlers

#### 2. components storage
O(n * m) where n is number of levels and m is the number of components available in one level

#### 3. add_handler
O(n) It includes split_path and insert in the Class RouteTrieNode. O(n + n) = O(2n) = O(n)

#### 4. lookup
O(n+m) It include a initial node, split_path function requirement, a for loop with check . O(n + m) where m is number of children need to be checked and n is number of component. 
Essentially, worst case need to check all existing path available(if consider total is n) if there is not any common components among them.

#### 5. split_path
O(n) It need "path_list" as a temporary storage to store all the components