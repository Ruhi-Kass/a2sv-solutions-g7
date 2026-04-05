class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        clones = {}
        node = head
        
        while node:
            clones[node] = Node(node.val)
            node = node.next
            
        node = head
        while node:
            clones[node].next = clones.get(node.next)
            clones[node].random = clones.get(node.random)
            node = node.next
            
        return clones[head]
