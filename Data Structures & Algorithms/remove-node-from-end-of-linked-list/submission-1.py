# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ## Remove Nth Node From End — Steps

        # 1. **Create a dummy node** before `head`.
        # 2. **Set two pointers:** `left = dummy`, `right = head`.
        # 3. **Move `right` N steps forward** to create an `N`-node gap.
        # 4. **Move both `left` and `right` together** until `right` reaches the end.
        # 5. Now **`left` is just before the node to remove**.
        # 6. **Skip the target node:** `left.next = left.next.next`.
        # 7. **Return `dummy.next`** as the new head.

        # ### Memory line

        # **Dummy → N gap → Move together → Left before target → Skip → Return**


        dummy = ListNode(0, head)
        left = dummy
        right = head
        while n > 0 and right:
            right = right.next
            n -= 1
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next

        