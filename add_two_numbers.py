# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp = ListNode(0)
        current = temp
        carry = 0
        while l1 or l2 or carry > 0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            sum = l1_val + l2_val + carry
            current.next = ListNode(sum % 10)
            carry = sum // 10

            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return temp.next


if __name__ == "__main__":
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    while result:
        print(result.val, end=" ")
        result = result.next
