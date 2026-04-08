
class Node:
    def __init__(self, val=None, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        def flatten_helper(curr: 'Node') -> 'Node':
          
            tail = curr
            
            while curr:
                tail = curr
                
                
                if curr.child:
                    child_tail = flatten_helper(curr.child)
                  
                    next_node = curr.next
                    
                 
                    curr.next = curr.child
                    curr.child.prev = curr
             
                    if next_node:
                        child_tail.next = next_node
                        next_node.prev = child_tail
            
                    curr.child = None
                    
                 
                    curr = child_tail
                else:
                    curr = curr.next
            
            return tail
        
     
        flatten_helper(head)
        return head
