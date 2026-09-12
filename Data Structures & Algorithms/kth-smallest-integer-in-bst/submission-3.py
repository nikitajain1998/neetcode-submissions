# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        while curr:
            if curr.left == None:
                k -= 1
                if k==0:
                    return curr.val
                curr = curr.right
            else:
                p = curr.left
                while p.right != None and p.right != curr:
                    p = p.right
                if p.right == None:
                    p.right = curr
                    curr = curr.left
                else:
                    k -= 1
                    if k== 0:
                        return curr.val
                    p.right = None
                    curr = curr.right 

        