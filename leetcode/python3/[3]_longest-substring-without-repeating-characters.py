#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
  '''
  Time Limit Exceeded
  986/987 cases passed (N/A)

  Time complexity : O(n^3)
  Space complexity : O(min(m,n)) where m is the size of the charset
  '''
  def lengthOfLongestSubstring(self, s: str) -> int:
    longest = 0

    for i in range(len(s)):
      for j in range(i, len(s)):
        chars = set()
        dup = False
        for k in range(i, j + 1):
          if s[k] in chars:
            longest = max(k - i, longest)
            dup = True
            break
          chars.add(s[k])
        
        if not dup:
          longest = max(j - i + 1, longest)
    
    return longest


  '''
  Accepted
  987/987 cases passed (56 ms)
  Your runtime beats 83.05 % of python3 submissions
  Your memory usage beats 55.44 % of python3 submissions (14.3 MB)

  Time complexity : O(n)
  Space complexity : O(min(m,n)) where m is the size of the charset
  '''
  def lengthOfLongestSubstring(self, s: str) -> int:
    d = dict()
    start, length = 0, 0

    for i in range(len(s)) :
      if s[i] in d:
        start = max(d[s[i]] + 1, start)
      
      d[s[i]] = i
      length = max(i - start + 1, length)
    
    return length
# @lc code=end

