# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(node):
            if not node:
                return 0
            
            lmax = dfs(node.left)
            rmax = dfs(node.right)
            lmax = max(lmax,0)
            rmax = max(rmax, 0)
            res[0] = max(res[0], node.val+ lmax + rmax)
            return node.val + max(lmax, rmax)
        
        dfs(root)
        return res[0]
        