# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

# It uses a famous technique called Floyd’s Cycle Detection Algorithm, also known as the slow and fast pointer technique.
# The trick is to use two pointers:]
# slow moves 1 step at a time.
# fast moves 2 steps at a time.
# If there's a cycle, eventually fast will catch up with slow.

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        