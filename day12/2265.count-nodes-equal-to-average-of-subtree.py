#
# @lc app=leetcode id=2265 lang=python3
#
# [2265] Count Nodes Equal to Average of Subtree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        def postorder(node):
            if not node.left and not node.right:                
                self.count += 1                
                return node.val, 1
            s1,n1 = 0,0
            s2, n2 = 0,0
            if node.left:
                s1, n1 = postorder(node.left)               
            if node.right:
                s2, n2 = postorder(node.right)
            
            ssum = (s1 + s2 + node.val) 

            if ssum // (n1+n2+1) == node.val:
                self.count += 1
            
            return ssum, n1+n2+1

        postorder(root)
        return self.count
        
# @lc code=end

