# Problem 3: Huffman Encoding

import sys
import heapq

class Node:
    def __init__(self, value=None, frequency = 0, left=None, right=None):
        self.value = value
        self.frequency = frequency
        self.left = left
        self.right = right
        
    def __gt__(self, other):
        if not other:
            return -1
        if not isinstance(other, Node):
            return -1
        return self.frequency > other.frequency
        
def build_huffman_tree(data):   
    # Step 1: Sort Frequency Table
    frequency = frequency_count(data)
    
    # Step 2: Use heap
    min_heap = min_heapify_dict(frequency)
    
    # Step 3: Build the Huffman Tree
    if len(min_heap) == 1:
        node = heapq.heappop(min_heap)
        new_node = Node(value = None, frequency = node.frequency)
        new_node.left = node
        heapq.heappush(min_heap, new_node)
        
    while len(min_heap) > 1:
        node1 = heapq.heappop(min_heap)
        node2 = heapq.heappop(min_heap)

        new_node = Node(value = None, frequency = node1.frequency + node2.frequency)
        new_node.left = node1
        new_node.right = node2

        heapq.heappush(min_heap, new_node)
    
    huffman_tree = heapq.heappop(min_heap)
    
    return huffman_tree
    
def frequency_count(data):
    frequency_table = {}
    
    for char in data:
        if char in frequency_table.keys():
            frequency_table[char] += 1
        else:
            frequency_table[char] = 1
            
    return frequency_table

def min_heapify_dict(frequency):
    heap = []
    for key in frequency:
        node = Node(key, frequency[key])
        heapq.heappush(heap, node)
    return heap


def code_generation_recursively(root, cur_code):
    codes = {}
    
    # Check if it is the last code
    if root is None:
        return {}
    
    # Set the current code with root char
    if root.value is not None:
        codes[root.value] = cur_code

    codes.update(code_generation_recursively(root.left, cur_code + "0"))
    codes.update(code_generation_recursively(root.right, cur_code + "1"))
    
    return codes

def huffman_encoding(data):
    # Check if the string is empty
    if data == "" or data is None:
        return "", None  
    
    # Get Huffman Tree
    huffman_tree = build_huffman_tree(data)
    
    # Check if the tree has <= 1 Node
    if huffman_tree.left is None and huffman_tree.right is None:
        return {huffman_tree.value:'0'}
    else:
        # Recursively make prefix
        codes = code_generation_recursively(huffman_tree, "")
        
    encoded_data = ""
    for char in data:
        encoded_data += codes[char]
        
    return encoded_data, huffman_tree

def huffman_decoding(encoded_text, tree):
    # Check if the encoded text is empty
    if encoded_text == "":
        return ""
    
    decoded_string = ""

    current_node = tree

    for char in encoded_text:
        if char == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right
            
        if current_node.value is not None:
            decoded_string += current_node.value
            current_node = tree
            
    return decoded_string  

# if __name__ == "__main__":
#     codes = {}

#     a_great_sentence = "The bird is the word"

#     print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
#     print ("The content of the data is: {}\n".format(a_great_sentence))

#     encoded_data, tree = huffman_encoding(a_great_sentence)

#     print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
#     print ("The content of the encoded data is: {}\n".format(encoded_data))

#     decoded_data = huffman_decoding(encoded_data, tree)

#     print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
#     print ("The content of the encoded data is: {}\n".format(decoded_data))
    
    
def test(string):
    if string in [None, "", " "]:
        print('The size of encoded data will not working')
        return None
    
    print ("The size of the data is: {}\n".format(sys.getsizeof(string)))
    print ("The content of the data is: {}\n".format(string))

    encoded_data, tree = huffman_encoding(string)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))
    
    return decoded_data

# Test Case 1
test_string1 = " "

test(test_string1)
# It will catch by the initial check and print error message

# Test Case 2
test_string2 = ""

test(test_string2)
# It will catch by the initial check and print error message

# Test Case 3
test_string3 = None

test(test_string3)
# It will catch by the initial check and print error message

# Test Case 4
# Source: Intro of Lord of Rings: The Rings of Power 
test_string4 = """
Beginning in a time of relative peace, we follow an ensemble cast of characters as they confront the re-emergence of 
evil to Middle-earth. From the darkest depths of the Misty Mountains, to the majestic forests of Lindon, 
to the breathtaking island kingdom of Númenor, to the furthest reaches of the map, 
these kingdoms and characters will carve out legacies that live on long after they are gone.
"""

test(test_string4)
# It will give same result.