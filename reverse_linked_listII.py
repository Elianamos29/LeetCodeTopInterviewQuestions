class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        if not head or left == right:
            return head

        temp = ListNode(0)
        temp.next = head
        prev = temp

        for _ in range(left - 1):
            prev = prev.next

        current = prev.next
        prev_reverse = None
        reverse_start = current

        for _ in range(right - left + 1):
            next_node = current.next
            current.next = prev_reverse
            prev_reverse = current
            current = next_node

        prev.next = prev_reverse
        reverse_start.next = current

        return temp.next


if __name__ == "__main__":
    # Example usage:
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    solution = Solution()
    new_head = solution.reverseBetween(head, 2, 4)
    current = new_head
    while current:
        print(current.val, end=" -> ")
        current = current.next
