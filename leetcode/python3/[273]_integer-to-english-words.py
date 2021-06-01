#
# @lc app=leetcode id=273 lang=python3
#
# [273] Integer to English Words
#

# @lc code=start
class Solution:
  '''
  Accepted
  601/601 cases passed (28 ms)
  Your runtime beats 89.28 % of python3 submissions
  Your memory usage beats 90.64 % of python3 submissions (14.2 MB)

  Time complexity : O(log n)
  Space complexity : O(n)
  '''
  def numberToWords(self, num: int) -> str:
    nums = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
    tens = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    exceptions = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    order = ['Thousand', 'Million', 'Billion', 'Trillion', 'Quadrillion', 'Quintillion', 'Sextillion',
             'Septillion', 'Octillion', 'Nonillion']
    
    if num == 0:
      return nums[0]

    retval = ''
    numStr = str(num)
    numStr = numStr.zfill((len(numStr) // 3) * 3 + 3)
    for i in range(len(numStr) // 3):
      if numStr[i * 3] != '0':
        retval += ' ' + nums[int(numStr[i * 3])] + ' ' + 'Hundred'
      if numStr[i * 3 + 1] == '1':
        retval += ' ' + exceptions[int(numStr[i * 3 + 1 : i * 3 + 3]) - 10]
      elif numStr[i * 3 + 1] == '0' and numStr[i * 3 + 2] != '0':
        retval += ' ' + nums[int(numStr[i * 3 + 2])]
      else:
        if numStr[i * 3 + 1] != '0':
          retval += ' ' + tens[int(numStr[i * 3 + 1]) - 2]
        if numStr[i * 3 + 2] != '0':
          retval += ' ' + nums[int(numStr[i * 3 + 2])]
      if int(numStr[i * 3 : i * 3 + 3]) > 0 and (len(numStr) // 3 - i - 2) >= 0:
        retval += ' ' + order[len(numStr) // 3 - i - 2]

    return retval.strip()
# @lc code=end

