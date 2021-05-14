#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
  '''
  Accepted
  601/601 cases passed (28 ms)
  Your runtime beats 83.1 % of python3 submissions
  Your memory usage beats 67.35 % of python3 submissions (14.2 MB)

  Time complexity : O(1)
  Space complexity : O(1)
  '''
  def hammingWeight(self, n: int) -> int:
    count = 0
    mask = 1
    for _ in range(32):
      if n & mask > 0:
        count += 1
      mask <<= 1
    
    return count
  

  '''
  Accepted
  601/601 cases passed (28 ms)
  Your runtime beats 83.1 % of python3 submissions
  Your memory usage beats 87.86 % of python3 submissions (14.1 MB)

  Time complexity : O(1)
  Space complexity : O(1)
  '''
  def hammingWeight(self, n: int) -> int:
    count = 0
    while n > 0:
      n &= (n - 1)
      count += 1

    return count
# @lc code=end

