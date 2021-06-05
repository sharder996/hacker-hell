#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
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
  33/33 cases passed (24 ms)
  Your runtime beats 97.49 % of python3 submissions
  Your memory usage beats 42.75 % of python3 submissions (14.5 MB)

  Time complexity : O(n)
  Space complexity : O(log n)
  '''
  def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    if root is None:
      return []

    retval = []
    stackLeft, stackRight = [root], list()
    while stackLeft or stackRight:
      temp = []
      while stackLeft:
        curr = stackLeft.pop()
        temp.append(curr.val)
        if curr.left:
          stackRight.append(curr.left)
        if curr.right:
          stackRight.append(curr.right)
      if temp:
        retval.append(temp)

      temp = []
      while stackRight:
        curr = stackRight.pop()
        temp.append(curr.val)
        if curr.right:
          stackLeft.append(curr.right)
        if curr.left:
          stackLeft.append(curr.left)
      if temp:
        retval.append(temp)
    
    return retval
# @lc code=end

