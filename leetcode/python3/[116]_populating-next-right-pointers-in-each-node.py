#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
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
  58/58 cases passed (72 ms)
  Your runtime beats 17.56 % of python3 submissions
  Your memory usage beats 90.44 % of python3 submissions (15.6 MB)
  
  Time complexity : O(n)
  Space complexity : O(log n)
  '''
  def connect(self, root: 'Node') -> 'Node':
    if root is None:
      return None
    
    stack = [root]
    while stack:
      temp = []
      while stack:
        curr = stack.pop(0)
        if stack:
          curr.next = stack[0]
        else:
          curr.next = None
        
        if curr.left:
          temp.append(curr.left)
        if curr.right:
          temp.append(curr.right)
      stack = temp

    return root
  

  '''
  Accepted
  58/58 cases passed (68 ms)
  Your runtime beats 30.1 % of python3 submissions
  Your memory usage beats 69.1 % of python3 submissions (15.7 MB)
  
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

