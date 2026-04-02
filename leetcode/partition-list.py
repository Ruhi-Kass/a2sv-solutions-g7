
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return None
        

        small_head = ListNode(0)
        small_tail = small_head
        large_head = ListNode(0)
        large_tail = large_head
        
        curr = head
        
        while curr:
            if curr.val < x:
                small_tail.next = curr
                small_tail = small_tail.next
            else:
                large_tail.next = curr
                large_tail = large_tail.next
            curr = curr.next
        
      
        large_tail.next = None
        
      
        small_tail.next = large_head.next
        
        return small_head.next
