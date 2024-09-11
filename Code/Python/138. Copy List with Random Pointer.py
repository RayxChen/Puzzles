class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head):
        if not head:
            return None
        
        copy_map = {}
        cur = head
        while cur:
            copy_map[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur:
            clone = copy_map[cur]
            if cur.next:
                clone.next = copy_map[cur.next]
            if cur.random:
                clone.random = copy_map[cur.random]
        return copy_map[head]