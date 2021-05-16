#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue:
  '''
  Accepted
  20/20 cases passed (36 ms)
  Your runtime beats 47.12 % of python3 submissions
  Your memory usage beats 41.26 % of python3 submissions (14.4 MB)

  Push:
  Time complexity : O(1)
  
  Pop:
  Time complexity : O(1)

  Peek:
  Time complexity : O(1)
  '''
  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.stack = list()
    self.reverseStack = list()

  def push(self, x: int) -> None:
    """
    Push element x to the back of queue.
    """
    self.stack.append(x)

  def pop(self) -> int:
    """
    Removes the element from in front of queue and returns that element.
    """
    if len(self.reverseStack) == 0:
      while len(self.stack) > 0:
        self.reverseStack.append(self.stack.pop())
    return self.reverseStack.pop()

  def peek(self) -> int:
    """
    Get the front element.
    """
    if len(self.reverseStack) > 0:
      return self.reverseStack[-1]
    else:
      while len(self.stack) > 0:
        self.reverseStack.append(self.stack.pop())
    return self.reverseStack[-1]

  def empty(self) -> bool:
    """
    Returns whether the queue is empty.
    """
    return len(self.stack) == 0 and len(self.reverseStack) == 0
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

