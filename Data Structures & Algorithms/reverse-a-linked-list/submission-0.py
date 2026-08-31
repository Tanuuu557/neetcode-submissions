class Node:
    def __init__(self, data = 0, next = None):
        self.data = data
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None 
        curr = head

        while curr:
            new_node = curr.next
            curr.next = prev
            prev = curr
            curr = new_node
        return prev
        