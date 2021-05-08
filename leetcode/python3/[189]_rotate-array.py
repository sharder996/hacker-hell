#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#
# def rotate(self, nums: List[int], k: int) -> None:
# @lc code=start
class Solution:
  '''
  Accepted
  37/37 cases passed (224 ms)
  Your runtime beats 28.48 % of python3 submissions
  Your memory usage beats 44.95 % of python3 submissions (25.4 MB)

  Time complexity : O(n)
  Space complexity : O(1)
  '''
  def rotate(self, nums, k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    def reverse(nums, start, end):
      while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
    
    k %= len(nums)
    if k:
      reverse(nums, len(nums) - k, len(nums) - 1)
      reverse(nums, 0, len(nums) - k - 1)
      reverse(nums, 0, len(nums) - 1)
  
  '''
  Time Limit Exceeded
  34/37 cases passed (N/A)
  
  Time complexity : O(n^2)
  Space complexity : O(1)
  '''
  def rotate(self, nums, k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    k %= len(nums)
    if k <= len(nums) - k:
      for _ in range(k):
        temp = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
          nums[i + 1] = nums[i]
        nums[0] = temp
    else:
      for _ in range(len(nums) - k):
        temp = nums[0]
        for i in range(1, len(nums)):
          nums[i - 1] = nums[i]
        nums[-1] = temp
    print(nums)
# @lc code=end
