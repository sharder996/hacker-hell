#
# @lc app=leetcode id=591 lang=python3
#
# [591] Tag Validator
#

# @lc code=start
class Solution:
  '''
  Accepted
  259/259 cases passed (28 ms)
  Your runtime beats 85.29 % of python3 submissions
  Your memory usage beats 72.55 % of python3 submissions (14.2 MB)

  Time complexity : O(n)
  Space complexity : O(n)
  '''
  def isValid(self, code: str) -> bool:
    stack = list()
    i = 0
    while i < len(code):
      if not stack and i > 0:
        return False
      
      if code[i:i+9] == '<![CDATA[':
        i = code.find(']]>', i + 9)
        if i == -1:
          return False
        i += 3
        continue

      if code[i:i+2] == '</':
        j = code.find('>', i + 2)
        if j == -1:
          return False
        if stack and stack[-1] == code[i+2:j]:
          stack.pop()
          i = j
        else:
          return False
        i += 1
        continue

      if code[i] == '<':
        j = code.find('>', i + 1)
        if j == -1 or j == i + 1 or j - i > 10:
          return False
        for t in code[i+1:j]:
          if not t.isupper():
            return False
        stack.append(code[i+1:j])
        i = j
      
      i += 1

    return len(stack) == 0
# @lc code=end

