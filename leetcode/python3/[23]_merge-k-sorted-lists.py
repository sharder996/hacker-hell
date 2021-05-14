#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
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
  133/133 cases passed (112 ms)
  Your runtime beats 54.35 % of python3 submissions
  Your memory usage beats 92.1 % of python3 submissions (17.7 MB)
  
  Time complexity : O(n log k)
  Space complexity : O(1)
  '''
  def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    if len(lists) == 0:
      return None
    
    while len(lists) > 1:
      for i in range(0, len(lists), 2):
        if i == len(lists) - 1:
          lists[i] = self.merge(lists[i], None)
        else:
          lists[i] = self.merge(lists[i], lists[i + 1])
      lists = lists[0::2]
    
    return lists[0]
  
  def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
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

