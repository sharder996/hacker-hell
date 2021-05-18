#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
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
  55/55 cases passed (16 ms)
  Your runtime beats 99.92 % of python3 submissions
  Your memory usage beats 98.79 % of python3 submissions (13.9 MB)

  Time complexity : O(n)
  Space complexity : O(1)
  '''
  def swapPairs(self, head: ListNode) -> ListNode:
    if head is None or head.next is None:
      return head
    
    prev = None
    curr = head
    currNext = head.next
    head = currNext
    while curr is not None and currNext is not None:
      curr.next = currNext.next
      currNext.next = curr
      if prev is not None:
        prev.next = currNext

      prev = curr
      curr = curr.next
      if curr is not None:
        currNext = curr.next
      
    return head
# @lc code=end

