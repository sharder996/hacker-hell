#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
  '''
  Accepted
  19/19 cases passed (48 ms)
  Your runtime beats 92.29 % of python3 submissions
  Your memory usage beats 46.68 % of python3 submissions (17.6 MB)
  
  Time complexity : O(n)
  Space complexity : O(1)
  '''
  def hasCycle(self, head: ListNode) -> bool:
    if head is None or head.next is None:
      return False
    
    slowPointer = head
    fastPointer = head.next
    while slowPointer is not fastPointer:
      if fastPointer is None or fastPointer.next is None:
        return False
      
      slowPointer = slowPointer.next
      fastPointer = fastPointer.next.next
    
    return True
# @lc code=end

