#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
  '''
  Accepted
  211/211 cases passed (1108 ms)
  Your runtime beats 35.9 % of python3 submissions
  Your memory usage beats 80.21 % of python3 submissions (25.1 MB)

  Time complexity : O(n)
  Space complexity : O(1)
  '''
  def maxProfit(self, prices: List[int]) -> int:
    if len(prices) == 1:
      return 0

    maxProfit = 0
    low = prices[0]
    for i in range(1, len(prices)):
      low = min(low, prices[i])
      maxProfit = max(maxProfit, prices[i] - low)
    
    return maxProfit
# @lc code=end

