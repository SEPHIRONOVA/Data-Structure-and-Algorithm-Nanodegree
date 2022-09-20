## Explanation_3: Huffman Coding

_Data Structure:_

- 'Heap': For this Huffman Coding problem I decided to use a min heap to allow for easy merging of the frequency nodes. I used Pythons heapq library to make the addition and removal of nodes easier.
- 'Tree': The Tree structed is used to construct Huffman Tree Structure

_Time Complexity:_

The Time Complexity of Encoding: 1. Frequency Count O(n) 2. Create Min Heap Dict O(n) 3. Push all into the tree O(n) 4. Encode all data for each char O(n) => O(n)
The Time Complexity of Decoding: Similarly it is also O(n)

To sum up, the time complexity is O(n)

_Space Complexity:_
O(k) where k is the distinct character used in the text.
