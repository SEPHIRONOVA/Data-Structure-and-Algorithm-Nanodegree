# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)
        self.handler = handler

    def insert(self, path_list, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.root
        
        # Iterate all children
        for path in path_list:
            if path not in node.children:
                node.insert(path)
            node = node.children[path]
        node.handler = handler

    def find(self, path_list):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        
        # Check if the root is initialized properly
        if self.root is None:
            return self.not_found_handler
     
        node = self.root
        
        # Iterate all children
        for path in path_list:
            if path not in node.children:
                return self.not_found_handler
            node = node.children[path]
        return node.handler
 
# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler
        
    def insert(self, path, handler=None):
        # Insert the node as before
        self.children[path] = RouteTrieNode(handler)       
        
# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler=None, not_found_handler=None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.root = RouteTrie(handler)
        self.handler = handler
        self.not_found_handler = not_found_handler if not_found_handler != "" or not_found_handler is not None else "not found handler"
        
    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        node = self.root
        path_list = self.split_path(path)
        node.insert(path_list, handler)
        
    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        
        # handle just slash
        if path == '/':
            return "root handler"
     
        node = self.root.root
        path_list = self.split_path(path)
        
        # Handle None type path_list(may occur after split)
        if path_list is None:
               return None
        
        for part in path_list:
            if part not in node.children:
                return "not found handler"
            node = node.children[part]
        if not node.handler:
            return "not found handler"
     
        return node.handler
 
    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        
        # Check if the path input is of correct type
        if path is None or type(path) != str:
               return None
        
        # Check if the path is at root or empty
        if path == '/' or path == '':
            return []
              
        path_list = path.split('/')

        # discard the empty strings
        if path_list[0] == '':
            path_list = path_list[1:]
            
        if path_list[-1] == '':
            path_list = path_list[:-1]
            
        return path_list        

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one

# Edge Case
print(router.lookup("")) # should print "root handler"
print(router.lookup(None)) # should print "None"
