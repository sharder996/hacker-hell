#
# @lc app=leetcode id=654 lang=python3
#
# [654] Maximum Binary Tree
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
  107/107 cases passed (220 ms)
  Your runtime beats 37.28 % of python3 submissions
  Your memory usage beats 30.86 % of python3 submissions (14.9 MB)

  Time complexity : O(n^2)
  Space complexity : O(n)
  '''
  def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
    if len(nums) == 0:
      return None

    maxVal = -1
    position = -1
    for i in range(len(nums)):
      if nums[i] > maxVal:
        maxVal = nums[i]
        position = i
    
    return TreeNode(maxVal, 
                    self.constructMaximumBinaryTree(nums[:position]), 
                    self.constructMaximumBinaryTree(nums[position+1:]))
  

  '''
  Accepted
  107/107 cases passed (192 ms)
  Your runtime beats 85.01 % of python3 submissions
  Your memory usage beats 30.86 % of python3 submissions (15 MB)

  Time complexity : O(n)
  Space complexity : O(n)
  '''
  def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
    if len(nums) == 0:
      return None
    
    stack = list()
    for i in range(len(nums)):
      curr = TreeNode(nums[i])
      while len(stack) > 0 and stack[-1].val < curr.val:
        curr.left = stack.pop()
      
      if len(stack) > 0:
        stack[-1].right = curr
      stack.append(curr)
    
    return stack[0]
# @lc code=end

