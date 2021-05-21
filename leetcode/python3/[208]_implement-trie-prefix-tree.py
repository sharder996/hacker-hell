#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#

# @lc code=start
class TrieNode:
  def __init__(self, val, next):
    self.val = val
    self.next = next
    self.terminal = False

class Trie:
  '''
  Accepted
  15/15 cases passed (176 ms)
  Your runtime beats 65.22 % of python3 submissions
  Your memory usage beats 41.98 % of python3 submissions (31.7 MB)

  Insertion:
  Time complexity : O(m) where m is the length of the string

  Search:
  Time complexity : O(m) where m is the length of the string
  '''
  def __init__(self):
    """
    Initialize your data structure here.
    """
    self.root = TrieNode(None, {})

  def insert(self, word: str) -> None:
    """
    Inserts a word into the trie.
    """
    curr = self.root
    for c in word:
      if c in curr.next:
        curr = curr.next[c]
      else:
        curr.next[c] = TrieNode(c, {})
        curr = curr.next[c]
    curr.terminal = True

  def search(self, word: str) -> bool:
    """
    Returns if the word is in the trie.
    """
    curr = self.root
    for c in word:
      if c not in curr.next:
        return False
      curr = curr.next[c]
    return curr.terminal

  def startsWith(self, prefix: str) -> bool:
    """
    Returns if there is any word in the trie that starts with the given prefix.
    """
    curr = self.root
    for c in prefix:
      if c not in curr.next:
        return False
      curr = curr.next[c]
    return True
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

