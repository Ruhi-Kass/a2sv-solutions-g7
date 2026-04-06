
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> list[ListNode]:
        if not head:
            return [None] * k
            

        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        
  
        part_size = n // k
        extra = n % k
        
        result = [None] * k
        curr = head
        
        for i in range(k):
            if not curr:
                break
                
            result[i] = curr
            current_part_size = part_size + (1 if i < extra else 0)
            
           
            for _ in range(current_part_size - 1):
                if curr:
                    curr = curr.next
            
          
            if curr:
                next_node = curr.next
                curr.next = None
                curr = next_node
        
        return result
