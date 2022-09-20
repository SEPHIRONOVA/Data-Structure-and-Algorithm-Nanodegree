# Problem 6: Union and Intersection
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def get_size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size
    
    def to_list(self):
        output = []
        node = self.head
        while node:
            output.append(node.value)
            node = node.next
            
        return output

def union(llist_1, llist_2):
    
    # Check if any of llist1 and llist2 is empty
    if llist_1.get_size() == 0:
        if llist_2.get_size() == 0:
            print("Both Linked List are empty.")
            return LinkedList()
        else:
            return llist_2
    else:
        if llist_2.get_size() == 0:
            return llist_1
    
    new_list_1 = llist_1.to_list()
    new_list_2 = llist_2.to_list()
    
    output_list = LinkedList()
    
    for item in new_list_1.copy():
        output_list.append(item)
        if item not in new_list_2:
            # Remove the first occurence of value only from list 1
            new_list_1.remove(item)
        else:
            # Remove the first occurence of value from both list            
            new_list_1.remove(item)
            new_list_2.remove(item)
    
    # Add Remaining item in list 2 if any
    for item in new_list_2:
        output_list.append(item)
    
    return output_list
    
# O(n + n + n*n + n) = O(3n + n*n) = O(n^2)
    
def intersection(llist_1, llist_2):
    
    # Check if any of llist1 and llist2 is empty
    if llist_1.get_size() == 0 or llist_2.get_size() == 0:
        print("At least one of the Linked List is empty.")
        return LinkedList() 

    new_list_1 = llist_1.to_list() 
    new_list_2 = llist_2.to_list()
    
    output_list = LinkedList()
    
    for item in new_list_2.copy():
        if item in new_list_1:
            output_list.append(item)
            # Remove the first occurence of value
            new_list_1.remove(item)
    
    return output_list

# Test Case 1
linked_list_1_1 = LinkedList()
linked_list_1_2 = LinkedList()

element_1_1 = []
element_1_2 = []

for i in element_1_1:
    linked_list_1_1.append(i)

for i in element_1_2:
    linked_list_1_2.append(i)

print("\nTest Case 1")
print(union(linked_list_1_1,linked_list_1_2))
# "Both Linked List are empty."
print(intersection(linked_list_1_1,linked_list_1_2))
# "At least one of the Linked List is empty."

# Test Case 2
linked_list_2_1 = LinkedList()
linked_list_2_2 = LinkedList()

element_2_1 = [3,4,5]
element_2_2 = []

for i in element_2_1:
    linked_list_2_1.append(i)

for i in element_2_2:
    linked_list_2_2.append(i)

print("\nTest Case 2")
print(union(linked_list_2_1,linked_list_2_2))
# "3 -> 4 -> 5 ->" which is the same as linked list 2_1
print(intersection(linked_list_2_1,linked_list_2_2))
# "At least one of the Linked List is empty."

# Test Case 3
linked_list_3_1 = LinkedList()
linked_list_3_2 = LinkedList()

element_3_1 = [1, 2, 3, 4, 5, 5, 6, 6, 7, 7, 8]
element_3_2 = [8, 8, 8, 1, 4, 4, 5, 7]

for i in element_3_1:
    linked_list_3_1.append(i)

for i in element_3_2:
    linked_list_3_2.append(i)

print("\nTest Case 3")
print(union(linked_list_3_1,linked_list_3_2))
# 1 -> 2 -> 3 -> 4 -> 5 -> 5 -> 6 -> 6 -> 7 -> 7 -> 8 -> 8 -> 8 -> 4 -> 
print(intersection(linked_list_3_1,linked_list_3_2))
# 8 -> 1 -> 4 -> 5 -> 7 -> 
