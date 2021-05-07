#
# @lc app=leetcode id=237 lang=python3
#
# [237] Delete Node in a Linked List
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
  41/41 cases passed (40 ms)
  Your runtime beats 55.63 % of python3 submissions
  Your memory usage beats 96.1 % of python3 submissions (14.6 MB)
  
  Time complexity : O(n)
  Space complexity : O(1)
  '''
  def deleteNode(self, node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    curr = node
    while curr.next is not None:
      curr.val = curr.next.val
      if curr.next.next is None:
        curr.next = None
      else:
        curr = curr.next
# @lc code=end
