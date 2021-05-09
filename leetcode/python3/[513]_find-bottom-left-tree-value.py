#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  '''
  Accepted
  76/76 cases passed (36 ms)
  Your runtime beats 93.81 % of python3 submissions
  Your memory usage beats 7.41 % of python3 submissions (17.3 MB)
  
  Time complexity : O(n)
  Space complexity : O(log n)
  '''
  def findBottomLeftValue(self, root: TreeNode) -> int:
    def findBottomLeftValueHelper(self, node: TreeNode, currDepth: int):
      nonlocal retval
      nonlocal depth

      if node.left is not None:
        findBottomLeftValueHelper(self, node.left, currDepth + 1)
      if node.right is not None:
        findBottomLeftValueHelper(self, node.right, currDepth + 1)
      if node.left is None and node.right is None and currDepth > depth:
        retval = node.val
        depth = currDepth

    retval, depth = 0, -1
    findBottomLeftValueHelper(self, root, 0)
    
    return retval
# @lc code=end

