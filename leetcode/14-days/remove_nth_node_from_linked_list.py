class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        size = 1

        while node.next != None:
            size += 1
            node = node.next
        
        nth = size - n

        if nth == 0:
            if head.next == None:
                return None
            else:
                head = head.next
                return head

        cnt = 1
        node = head

        while cnt != nth:
            node = node.next
            cnt += 1

        if node.next.next == None:
            node.next = None
        else:
            node.next = node.next.next
        return head