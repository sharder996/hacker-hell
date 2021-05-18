#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
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
  196/196 cases passed (32 ms)
  Your runtime beats 77.91 % of python3 submissions
  Your memory usage beats 69.7 % of python3 submissions (14.4 MB)

  Time complexity : O(n)
  Space complexity : O(log n)
  '''
  def isSymmetric(self, root: TreeNode) -> bool:
    leftSide = list()
    rightSide = list()

    l = root.left
    r = root.right
    while 1:
      if l is None and r is not None or l is not None and r is None:
        break
      if l is not None and r is not None and l.val != r.val:
        break

      if l is not None:
        leftSide.append(l.left)
      if l is not None:
        leftSide.append(l.right)
      if r is not None:
        rightSide.append(r.right)
      if r is not None:
        rightSide.append(r.left)

      if len(leftSide) == 0 or len(rightSide) == 0:
        break
      l = leftSide.pop(0)
      r = rightSide.pop(0)
    
    return l == r


  '''
  Accepted
  196/196 cases passed (28 ms)
  Your runtime beats 93.07 % of python3 submissions
  Your memory usage beats 89.22 % of python3 submissions (14.2 MB)

  Time complexity : O(n)
  Space complexity : O(log n)
  '''
  def isSymmetric(self, root: TreeNode) -> bool:
    def traverse(left: TreeNode, right: TreeNode) -> bool:
      if left is None and right is not None or left is not None and right is None:
        return False
      elif left is None and right is None:
        return True
      
      if left.val == right.val:
        return traverse(left.left, right.right) and traverse(left.right, right.left)
      else:
        return False
      
    return traverse(root.left, root.right)
# @lc code=end

