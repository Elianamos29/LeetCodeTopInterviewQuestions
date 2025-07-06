class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None

        old_to_new = {}
        current = head
        while current:
            old_to_new[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            new_node = old_to_new[current]
            new_node.next = old_to_new.get(current.next)
            new_node.random = old_to_new.get(current.random)
            current = current.next

        return old_to_new[head]


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node1.next = node2
    node1.random = node2
    node2.random = node1

    solution = Solution()
    copied_list_head = solution.copyRandomList(node1)

    current = copied_list_head
    while current:
        print(
            f"Node value: {current.val}, Random value: {current.random.val if current.random else None}"
        )
        current = current.next
