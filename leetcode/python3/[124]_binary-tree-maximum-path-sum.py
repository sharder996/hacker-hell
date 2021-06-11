#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
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
  94/94 cases passed (108 ms)
  Your runtime beats 17.51 % of python3 submissions
  Your memory usage beats 52.79 % of python3 submissions (21.7 MB)

  Time complexity : O(n)
  Space complexity : O(log n)
  '''
  def maxPathSum(self, root: TreeNode) -> int:
    def maxPathSumHelper(node: TreeNode) -> int:
      nonlocal globalMax
      if node is None:
        return 0
      
      left = maxPathSumHelper(node.left)
      right = maxPathSumHelper(node.right)

      retval = max(max(left, right) + node.val, node.val)
      maxi = max(retval, left + right + node.val)

      if maxi > globalMax:
        globalMax = maxi

      return retval

    globalMax = -2147483648
    maxPathSumHelper(root)

    return globalMax
# @lc code=end

