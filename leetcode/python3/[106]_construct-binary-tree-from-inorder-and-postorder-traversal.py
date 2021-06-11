#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
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
  202/202 cases passed (424 ms)
  Your runtime beats 6.37 % of python3 submissions
  Your memory usage beats 77.43 % of python3 submissions (18.8 MB)

  Time complexity : O(n)
  Space complexity : O(n)
  '''
  def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    def buildTreeHelper(index: int, start: int, end: int) -> TreeNode:
      if index < 0 or start > end:
        return None
      
      root = TreeNode(postorder[index])
      for i in range(len(postorder) - 1, -1, -1):
        if inorder[i] == root.val:
          break
      
      root.left = buildTreeHelper(index - 1 - end + i, start, i - 1)
      root.right = buildTreeHelper(index - 1, i + 1, end)

      return root
    
    return buildTreeHelper(len(postorder) - 1, 0, len(inorder) - 1)

    
  '''
  Accepted
  202/202 cases passed (52 ms)
  Your runtime beats 93.69 % of python3 submissions
  Your memory usage beats 51.49 % of python3 submissions (19.3 MB)

  Time complexity : O(n)
  Space complexity : O(n)
  '''
  def buildTree(self, inorder, postorder) -> TreeNode:
    def buildTreeHelper(iStart: int, iEnd: int, pStart: int, pEnd: int) -> TreeNode:
      if iStart > iEnd or pStart > pEnd:
        return None
      
      root = TreeNode(postorder[pEnd])
      root.left = buildTreeHelper(iStart, nodes[postorder[pEnd]] - 1, pStart, pStart + nodes[postorder[pEnd]] - iStart - 1)
      root.right = buildTreeHelper(nodes[postorder[pEnd]] + 1, iEnd, pStart + nodes[postorder[pEnd]] - iStart, pEnd - 1)

      return root

    nodes = dict()
    for i in range(len(inorder)):
      nodes[inorder[i]] = i
    
    return buildTreeHelper(0, len(inorder) - 1, 0, len(postorder) - 1)
# @lc code=end

