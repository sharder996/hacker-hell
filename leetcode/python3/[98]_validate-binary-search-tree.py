#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
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
  80/80 cases passed (44 ms)
  Your runtime beats 66.68 % of python3 submissions
  Your memory usage beats 51.66 % of python3 submissions (16.4 MB)

  Time complexity : O(n)
  Space complexity : O(log n)
  '''
  def isValidBST(self, root: TreeNode) -> bool:
    return self.isValidBSTHelper(root, pow(-2, 31) - 1, pow(2, 31))

  def isValidBSTHelper(self, node: TreeNode, mini: int, maxi: int) -> bool:
    if node is None:
      return True
    
    if node.val < mini or node.val > maxi:
      return False
    
    return self.isValidBSTHelper(node.left, mini, node.val - 1) and \
           self.isValidBSTHelper(node.right, node.val + 1, maxi)
# @lc code=end

