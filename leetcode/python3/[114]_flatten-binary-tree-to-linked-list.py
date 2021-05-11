#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
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
  225/225 cases passed (32 ms)
  Your runtime beats 91.7 % of python3 submissions
  Your memory usage beats 13.3 % of python3 submissions (15.3 MB)
  
  Time complexity : O(n)
  Space complexity : O(1)
  '''
  def flatten(self, root: TreeNode) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    if root is None or (root.right is None and root.left is None):
      return
    
    if root.left is not None:
      self.flatten(root.left)

      severedBranch = root.right
      root.right = root.left
      root.left = None

      temp = root.right
      while temp.right is not None:
        temp = temp.right
      
      temp.right = severedBranch
    
    self.flatten(root.right)
# @lc code=end

