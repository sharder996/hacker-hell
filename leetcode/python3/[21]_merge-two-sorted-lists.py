#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
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
  208/208 cases passed (40 ms)
  Your runtime beats 41.43 % of python3 submissions
  Your memory usage beats 61.83 % of python3 submissions (14.3 MB)
  
  Time complexity : O(m + n)
  Space complexity : O(m + n)
  '''
  def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if l1 is None:
      return l2
    if l2 is None:
      return l1
    
    if l1.val < l2.val:
      head = ListNode(l1.val)
      l1 = l1.next
    else:
      head = ListNode(l2.val)
      l2 = l2.next
    
    curr = head
    while l1 is not None or l2 is not None:
      if l1 is not None and l2 is not None and l1.val < l2.val or l2 is None:
        curr.next = ListNode(l1.val)
        l1 = l1.next
      else:
        curr.next = ListNode(l2.val)
        l2 = l2.next
      curr = curr.next
    
    return head


  '''
  Accepted
  208/208 cases passed (36 ms)
  Your runtime beats 72.33 % of python3 submissions
  Your memory usage beats 61.83 % of python3 submissions (14.2 MB)
  
  Time complexity : O(m + n)
  Space complexity : O(1)
  '''
  def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if l1 is None:
      return l2
    if l2 is None:
      return l1
    
    if l1.val < l2.val:
      head = l1
    else:
      head = l2
      l1, l2 = l2, l1

    while l1.next is not None:
      if l1.next.val > l2.val:
        temp = l1.next
        l1.next = l2
        l2 = temp
      l1 = l1.next
    
    l1.next = l2
    return head
# @lc code=end

