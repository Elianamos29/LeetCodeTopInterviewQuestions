class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        listMerged = ListNode(0)
        temp = listMerged
        while list1 or list2:
            if list1 is None:
                temp.next = list2
                list2 = list2.next
                temp = temp.next
            elif list2 is None:
                temp.next = list1
                list1 = list1.next
                temp = temp.next
            else:
                if list1.val <= list2.val:
                    temp.next = list1
                    list1 = list1.next
                else:
                    temp.next = list2
                    list2 = list2.next

                temp = temp.next

        return listMerged.next


if __name__ == "__main__":
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))
    solution = Solution()
    result = solution.mergeTwoLists(list1, list2)
    while result:
        print(result.val, end=" ")
        result = result.next
