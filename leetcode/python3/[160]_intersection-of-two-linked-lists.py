#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
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
  39/39 cases passed (160 ms)
  Your runtime beats 71.48 % of python3 submissions
  Your memory usage beats 42.71 % of python3 submissions (29.5 MB)

  Time complexity : O(n)
  Space complexity : O(1)
  '''
  def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    if headA is None or headB is None:
      return None
    
    currA, currB = headA, headB
    traversedA, traversedB = False, False
    while 1:
      if currA == currB:
        return currA
      
      if (currA is None or currB is None) and traversedA and traversedB:
        return None
      
      if currA is None:
        currA = headB
        traversedA = True
      else:
        currA = currA.next
      if currB is None:
        currB = headA
        traversedB = True
      else:
        currB = currB.next
# @lc code=end

