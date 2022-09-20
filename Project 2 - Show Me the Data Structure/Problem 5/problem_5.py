# Problem 5: Blockchain
import hashlib
import time

class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.previous_block = None
        self.hash = self.calc_hash()
    
    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = str(self.data).encode('utf-8')
        sha.update(hash_str)

        return sha.hexdigest()
    
    def __repr__(self):
        return 'Blockchain created at {} with content {}. And its hashvalue is {}'.format(self.timestamp, self.data, self.hash)
    
class BlockChain:
    def __init__(self):
        self.tail = None
        self.size = 0
        
    def append(self, value):
        if self.tail is None:
            self.tail = Block(time.gmtime(), value, None)
        else:
            # Assign None as initial hashvalue
            prev_hash = self.tail.previous_hash
            new_block = Block(time.gmtime(), value, prev_hash)
            new_block.previous_block = self.tail
            self.tail = new_block
            
        self.size += 1
    
    def get_size(self):
        return self.size
        
    def search(self, value):
        if self.tail is None:
            print("The Blockchain is Empty")
            return None
        else:
            pointer = self.tail
            while pointer:
                if pointer.data == value:
                    return pointer
                
                pointer = pointer.previous_block
                
            return None 
     
# Test
bc1 = BlockChain()

# Test Case 1 (Edge Case) - Empty Blockchain
print(bc1.get_size())
# The Blockchain is empty!
# 0

# Test Case 2 (Edge Case) - Add None as value to blockchain
bc1.append(None)
print(bc1.get_size())
# 1

# Test Case 3
bc1.append(15)
bc1.append("txt")
bc1.append("Harry Potter")

print(bc1.search(15))
# Block chain create at {time} with content 15. And its hasvalue is {hashvalue}
