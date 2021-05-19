#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
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
  116/116 cases passed (40 ms)
  Your runtime beats 80.29 % of python3 submissions
  Your memory usage beats 66.38 % of python3 submissions (15.9 MB)

  Time complexity : O(n)
  Space complexity : O(log n)
  '''
  def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
    if root is None:
      return False
    
    retval = False
    if root.right is None and root.left is None and root.val == targetSum:
      return True
    if root.left is not None:
      retval |= self.hasPathSum(root.left, targetSum - root.val)
    if root.right is not None:
      retval |= self.hasPathSum(root.right, targetSum - root.val)
    return retval
# @lc code=end

