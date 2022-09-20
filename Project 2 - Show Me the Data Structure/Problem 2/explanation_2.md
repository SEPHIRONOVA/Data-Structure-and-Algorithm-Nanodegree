## Explanation_2: File Recursion

_Data Structure:_

- 'List': It is used to store path for simiplicity

depth of directory: d
width of directory: w
number of files in a directory: n

_Time Complexity:_
O(d \* w) as it is dependent on number of directory and depth of the root directory

_Space Complexity:_
O(w + n) as the recursion function need to remember all the directory and all file/directory under current one
