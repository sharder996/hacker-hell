#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
  '''
  Accepted
  31/31 cases passed (76 ms)
  Your runtime beats 41.43 % of python3 submissions
  Your memory usage beats 82.57 % of python3 submissions (25.1 MB)

  Time complexity : O(n)
  Space complexity : O(1)
  '''
  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if root is None:
      return None
    
    if root.val == p.val or root.val == q.val:
      return root
    
    l = self.lowestCommonAncestor(root.left, p, q)
    r = self.lowestCommonAncestor(root.right, p, q)

    if r and l:
      return root
    return l if l is not None else r
# @lc code=end

