class DLListNode:
    def __init__(self, val):
        self.val = val
        self.front = None
        self.back = None

class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.cap = capacity
        self.c_dict = dict()
        self.q_head = None
        self.q_tail = None

    def printHead(self):
        n = self.q_head
        print "Printing Head == "
        while n != None:
            print n.val
            n = n.back
        print "================ "

    def removeNode(self, node):
        if node.front != None:
            node.front.back = node.back
        else:
            self.q_head = node.back
            
        if node.back != None:
            node.back.front = node.front
        else:
            self.q_tail = node.front
            
        node.back = None
        node.front = None
        
    def prependNode(self, node):
        if self.q_head == None:
            self.q_head = node
            self.q_tail = self.q_head
        else:
            self.q_head.front = node
            node.back = self.q_head
            self.q_head = node

    # @return an integer
    def get(self, key):
        if key not in self.c_dict:
            return -1
        
        #Delete node from the old position
        value, node = self.c_dict[key]
        self.removeNode(node)
        self.prependNode(node)
        return value

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key not in self.c_dict and len(self.c_dict) >= self.cap:
            del self.c_dict[self.q_tail.val]
            print self.q_tail.val
            if self.q_tail.front != None:
                self.q_tail = self.q_tail.front
                self.q_tail.back = None
            else:
                self.q_tail = None
                self.q_head = None
        
        if key in self.c_dict:
            #Delete a node from the old position
            node = self.c_dict[key][1]
            self.removeNode(node)
        else:
            #Create a node in the new position
            node = DLListNode(key)
            
        self.prependNode(node)
        self.c_dict[key] = [value, node]

if __name__ == "__main__":
    lru = LRUCache(2)
    lru.set(2, 1)
    lru.printHead()
    print lru.c_dict
    lru.set(1, 1)
    lru.printHead()
    print lru.c_dict
    lru.set(2, 3)
    lru.printHead()
    print lru.c_dict
    lru.set(4, 1)
    lru.printHead()
    print lru.c_dict
    print lru.get(1)
    lru.printHead()
    print lru.c_dict
    print lru.get(2)
    lru.printHead()
    print lru.c_dict
