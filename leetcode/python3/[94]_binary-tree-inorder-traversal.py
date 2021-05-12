#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
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
  68/68 cases passed (32 ms)
  Your runtime beats 52.82 % of python3 submissions
  Your memory usage beats 12.58 % of python3 submissions (14.3 MB)

  Time complexity : O(n)
  Space complexity : O(n)
  '''
  def inorderTraversal(self, root: TreeNode) -> List[int]:
    if root is None:
      return []
    
    retval = []
    retval += self.inorderTraversal(root.left)
    retval.append(root.val)
    retval += self.inorderTraversal(root.right)
    return retval
  

  '''
  Accepted
  68/68 cases passed (28 ms)
  Your runtime beats 80.72 % of python3 submissions
  Your memory usage beats 75.11 % of python3 submissions (14.1 MB)

  Time complexity : O(n)
  Space complexity : O(n)
  '''
  def inorderTraversal(self, root: TreeNode):
    if root is None:
      return []
    
    retval = []
    stack = [root]
    descending = True
    while len(stack) > 0:
      curr = stack.pop()
      if descending and curr.left is not None:
        stack.append(curr)
      while descending and curr.left is not None:
        curr = curr.left
        if curr.left is not None:
          stack.append(curr)
      
      retval.append(curr.val)
      if curr.right is not None:
        stack.append(curr.right)
        descending = True
      else:
        descending = False
    
    return retval
# @lc code=end

