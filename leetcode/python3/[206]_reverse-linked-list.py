#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
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
  28/28 cases passed (36 ms)
  Your runtime beats 61.72 % of python3 submissions
  Your memory usage beats 42.71 % of python3 submissions (15.7 MB)

  Time complexity : O(n)
  Space complexity : O(1)
  '''
  def reverseList(self, head: ListNode) -> ListNode:
    if head is None or head.next is None:
      return head
    
    prev = None
    curr = head
    while curr.next is not None:
      temp = curr.next
      curr.next = prev
      
      prev = curr
      curr = temp
    curr.next = prev

    return curr
# @lc code=end

