#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
  '''
  Accepted
  269/269 cases passed (24 ms)
  Your runtime beats 96.46 % of python3 submissions
  Your memory usage beats 95.57 % of python3 submissions (14 MB)

  Time complexity : O(n)
  Space complexity : O(n)
  '''
  def numDecodings(self, s: str) -> int:
    if s[0] == '0':
      return 0
    
    dp = [0] * (len(s) + 1)
    dp[0], dp[-1] = 1, 1

    for i in range(1, len(s)):
      if int(s[i]) > 0:
        dp[i] = dp[i - 1]
      if 10 <= int(s[i-1:i+1]) <= 26:
        dp[i] += dp[i-2]
    
    return dp[-2]
# @lc code=end

