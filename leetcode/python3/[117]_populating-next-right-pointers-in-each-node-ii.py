#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
  '''
  Accepted
  55/55 cases passed (48 ms)
  Your runtime beats 72.63 % of python3 submissions
  Your memory usage beats 94.83 % of python3 submissions (15.2 MB)
  
  Time complexity : O(n)
  Space complexity : O(1)
  '''
  def connect(self, root: 'Node') -> 'Node':
    def getNextRight(node: 'Node') -> 'None':
      node = node.next
      while node:
        if node.left:
          return node.left
        if node.right:
          return node.right
        node = node.next
      return None

    if root is None:
      return None
    
    curr = root
    curr.next = None
    while curr:
      temp = curr
      while temp:
        if temp.left:
          if temp.right:
            temp.left.next = temp.right
          else:
            temp.left.next = getNextRight(temp)
        if temp.right:
          temp.right.next = getNextRight(temp)
        
        temp = temp.next
      
      if curr.left:
        curr = curr.left
      elif curr.right:
        curr = curr.right
      else:
        curr = getNextRight(curr)
    
    return root
# @lc code=end

