#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
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
  62/62 cases passed (60 ms)
  Your runtime beats 10.24 % of python3 submissions
  Your memory usage beats 74.42 % of python3 submissions (15.2 MB)

  Time complexity : O(n)
  Space complexity : O(1)
  '''
  def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
    if k == 1:
      return head
    
    curr = head
    first = True
    tail = None
    while 1:
      temp = curr
      end = False
      for _ in range(k):
        if curr is None:
          end = True
          break
        curr = curr.next
      if end:
        break

      prev = curr
      tempHead = temp
      tempTail = temp
      for i in range(k):
        tempHead = temp.next
        temp.next = prev
        prev = temp
        temp = tempHead
      
      if tail is not None:
        tail.next = prev
      tail = tempTail

      if first:
        head = prev
        first = False

    return head
# @lc code=end

