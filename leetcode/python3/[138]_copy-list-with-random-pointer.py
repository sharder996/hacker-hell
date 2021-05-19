#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
# Definition for a Node.
# class Node:
#     def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
#         self.val = int(x)
#         self.next = next
#         self.random = random
class Solution:
  '''
  Accepted
  19/19 cases passed (36 ms)
  Your runtime beats 61 % of python3 submissions
  Your memory usage beats 25.19 % of python3 submissions (15.1 MB)

  Time complexity : O(n)
  Space complexity : O(n)
  '''
  def copyRandomList(self, head: 'Node') -> 'Node':
    if head is None:
      return None
    
    pointers = dict()
    pointersNew = []
    retval = None
    currNew = None
    curr = head
    length = 0
    while curr is not None:
      n = Node(curr.val)
      pointers[curr] = length
      pointersNew.append(n)
      
      if retval is None:
        retval = n
        currNew = retval
      else:
        currNew.next = n
        currNew = currNew.next

      curr = curr.next
      length += 1
      
    curr = head
    currNew = retval
    for i in range(length):
      if curr.random is not None:
        currNew.random = pointersNew[pointers[curr.random]]

      currNew = currNew.next
      curr = curr.next
      i += 1
    return retval


  '''
  Accepted
  19/19 cases passed (32 ms)
  Your runtime beats 85.73 % of python3 submissions
  Your memory usage beats 45.41 % of python3 submissions (15 MB)

  Time complexity : O(n)
  Space complexity : O(1)
  '''
  def copyRandomList(self, head: 'Node') -> 'Node':
    if head is None:
      return None
    
    curr = head
    while curr != None:
      new = Node(curr.val)
      new.next = curr.next
      curr.next = new
      curr = curr.next.next
 
    curr = head
    while curr != None:
      if curr.random is not None:
        curr.next.random = curr.random.next
      curr = curr.next.next
 
    curr = head
    retval = head.next
    while curr.next != None:
      tmp = curr.next
      curr.next = curr.next.next
      curr = tmp
 
    return retval
# @lc code=end

