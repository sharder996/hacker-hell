#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution:
  '''
  Accepted
  104/104 cases passed (216 ms)
  Your runtime beats 14.71 % of python3 submissions
  Your memory usage beats 42.75 % of python3 submissions (14.5 MB)

  Time complexity : O(n)
  Space complexity : O(1)
  '''
  def firstUniqChar(self, s: str) -> int:
    d = [0] * 26

    for i in range(len(s)):
      d[ord(s[i]) - ord('a')] += 1
    
    for i in range(len(s)):
      if d[ord(s[i]) - ord('a')] == 1:
        return i
    return -1
# @lc code=end

