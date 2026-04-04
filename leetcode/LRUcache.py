class ListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} 
        
        self.head = ListNode()  
        self.tail = ListNode()  
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _add_node(self, node: ListNode):
      
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def _remove_node(self, node: ListNode):
       
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev
    
    def _move_to_head(self, node: ListNode):
      
        self._remove_node(node)
        self._add_node(node)
    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_head(node)  
        return node.val
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
          
            node = self.cache[key]
            node.val = value
            self._move_to_head(node)
        else:
           
            new_node = ListNode(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)
            
        
            if len(self.cache) > self.capacity:
                lru = self.tail.prev
                self._remove_node(lru)
                del self.cache[lru.key]
