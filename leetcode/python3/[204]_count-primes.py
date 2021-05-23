#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
class Solution:
  '''
  Accepted
  21/21 cases passed (3756 ms)
  Your runtime beats 11.28 % of python3 submissions
  Your memory usage beats 15.46 % of python3 submissions (323.1 MB)

  Time complexity : O(n^1/2 log log n)
  Space complexity : O(n)
  '''
  def countPrimes(self, n: int) -> int:
    if n <= 2:
      return 0
    
    retval = 0
    sieve = set()
    for i in range(2, int(sqrt(n)) + 1):
      if i not in sieve:
        for j in range(i * i, n, i):
          sieve.add(j)
    
    return n - len(sieve) - 2
# @lc code=end

