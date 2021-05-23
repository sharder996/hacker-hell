#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
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
  27/27 cases passed (76 ms)
  Your runtime beats 70.41 % of python3 submissions
  Your memory usage beats 68.07 % of python3 submissions (18.2 MB)

  Time complexity : O(log n)
  Space complexity : O(1)
  '''
  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    curr = root
    while 1:
      if curr.val > max(p.val, q.val):
        curr = curr.left
      elif curr.val < min(p.val, q.val):
        curr = curr.right
      else:
        return curr
# @lc code=end

