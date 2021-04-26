#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
  '''
  Accepted
  53/53 cases passed (44 ms)
  Your runtime beats 83.5 % of python3 submissions
  Your memory usage beats 98.16 % of python3 submissions (14.1 MB)

  Time complexity : O(n^2)
  Space complexity : O(1)
  '''
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
      for j in range(len(nums)):
        if i != j:
          if nums[i] + nums[j] == target:
            return [i, j]
    
    return []
  

  '''
  Accepted
  53/53 cases passed (40 ms)
  Your runtime beats 94.95 % of python3 submissions
  Your memory usage beats 44.76 % of python3 submissions (14.5 MB)

  Time complexity : O(n)
  Space complexity : O(n)
  '''
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    d = dict()
    for i in range(len(nums)):
      if target - nums[i] in d:
        return [d[target - nums[i]], i]
      d[nums[i]] = i
    
    return []
# @lc code=end

