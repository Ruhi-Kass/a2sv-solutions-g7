
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        current = head
        while current.next:
            if current.val == current.next.val:
               
                current.next = current.next.next
            else:
               
                current = current.next
        
        return head
