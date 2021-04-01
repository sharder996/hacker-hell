#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
  '''
  Accepted
  1568/1568 cases passed (68 ms)
  Your runtime beats 73.55 % of python3 submissions
  Your memory usage beats 44.34 % of python3 submissions (14.4 MB)

  Time complexity : O(max(m,n))
  Space complexity : O(max(m,n))
  '''
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    l3 = list()
    curr = 0
    
    total = 0
    while l1 != None or l2 != None or total > 0:
      if l1 != None:
        total += l1.val
        l1 = l1.next
      
      if l2 != None:
        total += l2.val
        l2 = l2.next
      
      l3.append(ListNode(total % 10))
      if curr > 0:
        l3[curr - 1].next = l3[curr]
      total = int(total / 10)
      curr += 1
    
    return l3[0]
        
# @lc code=end

