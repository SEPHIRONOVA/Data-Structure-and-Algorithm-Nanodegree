# Problem 1 - LRU Cache

class DLLNode:
    def __init__(self, key=0, value=0, prev=None, next=None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRU_Cache(object):
    def __init__(self, capacity):
        # Initialize class variables    
        if capacity < 1:
            print ("Please enter a value greater than 0.")
        
        self.capacity = capacity
        self.cache = dict()
        self.nodes = None
        self.head = DLLNode() # Used to keep most recent
        self.tail = DLLNode() # Used to keep least recent 
        # Note: self.head -> node(most recently) -> ... -> node(least recently) -> self.tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        # Remove an existing node from LRU Cache
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        
    def insert(self, node):
        # Insert a new node into the head LRU Cache(Always head)
        self.head.next.prev = node
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        
    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if self.capacity == 0:
            return None
        
        if key in self.cache.keys():
            #Step 1: remove the node from linked list
            self.remove(self.cache[key])
            #Step 2: Add the node at the beginning of Cache
            self.insert(self.cache[key])
            return self.cache[key].value
        
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.capacity == 0:
            return None
        
        if key in self.cache.keys():
            self.cache[key].value = value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
        else:
            to_insert = DLLNode(key, value)
            if len(self.cache) >= self.capacity:
                lru = self.tail.prev
                self.remove(lru)
                del self.cache[lru.key]
            self.insert(to_insert)
            self.cache[key] = to_insert
            
# LRU Test
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);

#our_cache.get(1)       # returns 1
#our_cache.get(2)       # returns 2
#our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(1)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
print("\nTest Case 1:")
cache_1 = LRU_Cache(8)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);
our_cache.set(5, 5);
our_cache.set(6, 6);
our_cache.set(7, 7);
our_cache.set(8, 8);

print("Should be 4, 5, 5 respectively:")
print(our_cache.get(4)) # Should print 4
print(our_cache.get(5)) # Should print 5

print(our_cache.head.next.value) # should be 5

# Put 3 more to replace the first 3 entry
our_cache.set(9, 9);
our_cache.set(10, 10);
our_cache.set(11, 11); 

print("\nAll 3 below should be -1:")
# All 3 should print -1
print(our_cache.get(1))
print(our_cache.get(2))
print(our_cache.get(3))

our_cache.set(12, 12)

print("\nShould return -1 as 6 is being replaced due to 4, 5 moved ahead")
print(our_cache.get(6))

# Test Case 2
print("Should ask for entering a positive number:")
cache_2 = LRU_Cache(0)

print("\nTest Case 2:")
print("Should return None for 2 below:")
print(cache_2.set(1,1)) # Should return None as capacity = 0 
print(cache_2.get(1)) # Should return None as capacity = 0 

# Test Case 3
print("\nTest Case 3:")
cache_3 = LRU_Cache(2)

cache_3.set(1,1)
cache_3.set(2,2)

# Update key 2
cache_3.set(2,5)

print("Should print 5 instead of 1 if replace works:")
print(cache_3.get(2))

# Test Case 4
print("\nTest Case 4:")
cache_4 = LRU_Cache(0)