#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
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
  34/34 cases passed (36 ms)
  Your runtime beats 54.29 % of python3 submissions
  Your memory usage beats 87.84 % of python3 submissions (14.4 MB)

  Time complexity : O(n)
  Space complexity : O(n)
  '''
  def levelOrder(self, root: TreeNode) -> List[List[int]]:
    if root is None:
      return []
    
    retval = list()
    queue = [root]
    count = 1

    while len(queue) > 0:
      retval.append([])
      temp = count
      count = 0
      while temp > 0:
        curr = queue.pop(0)
        retval[-1].append(curr.val)
        temp -= 1

        if curr.left is not None:
          queue.append(curr.left)
          count += 1
        if curr.right is not None:
          queue.append(curr.right)
          count += 1

    return retval
# @lc code=end

