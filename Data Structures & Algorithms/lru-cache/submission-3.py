class Node:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = self.prev = None

class LRUCache:

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev

        node.next = self.right
        self.right.prev = node

    def __init__(self, capacity: int):
       self.cache = {}
       self.capacity = capacity

       self.left, self.right = Node(0, 0), Node(0, 0)
       self.left.next, self.right.prev = self.right, self.left

    def get(self, key: int) -> int: 
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


