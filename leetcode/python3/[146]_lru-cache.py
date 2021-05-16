#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class Node:
  def __init__(self, key: int, val: int):
    self.key = key
    self.val = val
    self.prev = None
    self.next = None

class LRUCache:
  '''
  Accepted
  20/20 cases passed (208 ms)
  Your runtime beats 42.12 % of python3 submissions
  Your memory usage beats 35.93 % of python3 submissions (23.8 MB)

  Insertion:
  Time complexity : O(1)
  
  Retrieval:
  Time complexity : O(1)
  '''
  def __init__(self, capacity: int):
    self.cache = dict()
    self.cap = capacity
    self.head = None
    self.tail = None

  def get(self, key: int) -> int:
    if key in self.cache:
      n =  self.cache[key]
      self._removeNode(n)
      self._insertNode(n)
      return n.val
    return -1

  def put(self, key: int, value: int) -> None:
    if key in self.cache:
      n =  self.cache[key]
      n.val = value
      self._removeNode(n)
      self._insertNode(n)
    else:
      if len(self.cache) >= self.cap:
        self.cache.pop(self.head.key)
        self._removeNode(self.head)
      n = Node(key, value)
      self._insertNode(n)
      self.cache[key] = n
  
  def _removeNode(self, n: Node):
    if n.prev is not None:
      n.prev.next = n.next
    else:
      self.head = n.next
    
    if n.next is not None:
      n.next.prev = n.prev
    else:
      self.tail = n.prev

  def _insertNode(self, n: Node):
    if self.tail is not None:
      self.tail.next = n

    n.prev = self.tail
    n.next = None
    self.tail = n
    if self.head is None:
      self.head = self.tail
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

