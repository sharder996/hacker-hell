#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
  '''
  Accepted
  168/168 cases passed (84 ms)
  Your runtime beats 73.11 % of python3 submissions
  Your memory usage beats 53.91 % of python3 submissions (16.1 MB)

  Time complexity : O(n log n)
  Space complexity : O(n)
  '''
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    retval = []
    intervals.sort(key=lambda x: x[0])

    start, end = intervals[0][0], intervals[0][1]
    for interval in intervals:
      if interval[0] <= end and interval[1] > end:
        end = interval[1]
      elif interval[0] > end:
        retval.append([start, end])
        start = interval[0]
        end = interval[1]
    retval.append([start, end])

    return retval
# @lc code=end

