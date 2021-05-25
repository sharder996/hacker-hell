#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class MinHeap:
  def __init__(self, nums, size: int):
    self.heap = nums
    self.size = size

    i = (size - 1) // 2
    while i >= 0:
      self.heapify(i)
      i -= 1
  
  def heapify(self, position: int):
    l = 2 * position + 1
    r = 2 * position + 2
    smallest = position
    if l < self.size and self.heap[l] < self.heap[position]:
      smallest = l
    if r < self.size and self.heap[r] < self.heap[smallest]:
      smallest = r
    if smallest != position:
      self.heap[position], self.heap[smallest] = self.heap[smallest], self.heap[position]
      self.heapify(smallest)
  
  def replaceMin(self, min: int):
    self.heap[0] = min
    self.heapify(0)
  
  def getMin(self):
    return self.heap[0]

class Solution:
  '''
  Accepted
  32/32 cases passed (92 ms)
  Your runtime beats 20.82 % of python3 submissions
  Your memory usage beats 74.05 % of python3 submissions (15 MB)

  Time complexity : O((n-k) * log k)
  Space complexity : O(k)
  '''
  def findKthLargest(self, nums: List[int], k: int) -> int:
    heap = []

    for i in range(k):
      heap.append(nums[i])
    
    for i in range(k, len(nums)):
      heap.sort()
      if nums[i] > heap[0]:
        heap.pop(0)
        heap.append(nums[i])
    
    heap.sort()
    return heap[0]


  '''
  Accepted
  32/32 cases passed (72 ms)
  Your runtime beats 30.69 % of python3 submissions
  Your memory usage beats 74.05 % of python3 submissions (15.1 MB)

  Time complexity : O((n-k) * log k)
  Space complexity : O(k)
  '''
  def findKthLargest(self, nums: List[int], k: int) -> int:
    heap = MinHeap(nums[:k], k)

    for i in range(k, len(nums)):
      if nums[i] > heap.getMin():
        heap.replaceMin(nums[i])
    
    return heap.getMin()
# @lc code=end

