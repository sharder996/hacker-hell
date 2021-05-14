#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
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
  1563/1563 cases passed (72 ms)
  Your runtime beats 99.55 % of python3 submissions
  Your memory usage beats 12.96 % of python3 submissions (14.4 MB)

  Time complexity : O(n)
  Space complexity : O(n)
  '''
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    num1, num2 = [], []

    while l1 is not None:
      num1.append(l1.val)
      l1 = l1.next
    
    while l2 is not None:
      num2.append(l2.val)
      l2 = l2.next
    
    retval = None
    carry = 0
    while len(num1) > 0 or len(num2) > 0:
      if len(num1) > 0 and len(num2) > 0:
        sum_ = num1.pop() + num2.pop()
      elif len(num1) > 0:
        sum_ = num1.pop()
      else:
        sum_ = num2.pop()
      
      retval = ListNode((sum_ + carry) % 10, retval)
      carry = (sum_ + carry) // 10
    
    if carry > 0:
      retval = ListNode(carry, retval)

    return retval
# @lc code=end

