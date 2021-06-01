#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
  '''
  Accepted
  61/61 cases passed (76 ms)
  Your runtime beats 50.14 % of python3 submissions
  Your memory usage beats 58.51 % of python3 submissions (20.6 MB)

  next:
  Time complexity : O(log n)
  
  hasNext:
  Time complexity : O(1)
  '''
  def __init__(self, root: TreeNode):
    self.stack = [root]
    self.descending = True

  def next(self) -> int:
    curr = self.stack.pop()
    if self.descending and curr.left is not None:
      self.stack.append(curr)
    while self.descending and curr.left is not None:
      curr = curr.left
      if curr.left is not None:
        self.stack.append(curr)
    
    retval = curr.val
    if curr.right is not None:
      self.stack.append(curr.right)
      self.descending = True
    else:
      self.descending = False

    return retval

  def hasNext(self) -> bool:
    return len(self.stack) > 0
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

