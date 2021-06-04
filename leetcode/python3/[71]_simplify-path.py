#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
  '''
  Accepted
  256/256 cases passed (28 ms)
  Your runtime beats 88.74 % of python3 submissions
  Your memory usage beats 71.98 % of python3 submissions (14.3 MB)

  Time complexity : O(n)
  Space complexity : O(n)
  '''
  def simplifyPath(self, path: str) -> str:
    path = path.split('/')

    stack = list()
    for address in path:
      if address == '..':
        if stack:
          stack.pop()
      elif len(address) > 2 or address.find('_') != -1 or address.lower().islower():
        stack.append(address)
    
    return '/' + '/'.join(stack).strip('/')
# @lc code=end

