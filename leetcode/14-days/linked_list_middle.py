# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        size = 1
        node = head

        while node.next != None:
            node = node.next
            size += 1
        
        cnt = 1
        node = head
        mid = int(size / 2) + 1

        while cnt != mid:
            node = node.next
            cnt += 1
        
        return node