#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
class TrieNode:
  def __init__(self, val: set, next):
    self.val = val
    self.next = next
    self.terminal = None

class Trie:
  def __init__(self):
    self.root = TrieNode(None, {})

  def insert(self, word: str) -> None:
    curr = self.root
    for c in word:
      if c in curr.next:
        curr = curr.next[c]
      else:
        curr.next[c] = TrieNode(c, {})
        curr = curr.next[c]
    curr.terminal = word
  
  def search(self, word: str) -> bool:
    curr = self.root
    for c in word:
      if c not in curr.next:
        return False
      curr = curr.next[c]
    return curr.terminal

class Solution:
  '''
  Accepted
  40/40 cases passed (6108 ms)
  Your runtime beats 50.63 % of python3 submissions
  Your memory usage beats 40.84 % of python3 submissions (14.7 MB)

  Time complexity : O((m * n)^2)
  Space complexity : O(w) where w is the length of words
  '''
  def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    def dfs(row: int, col: int, curr: TrieNode) -> None:
      if curr.terminal:
        retval.append(curr.terminal)
        curr.terminal = None

      if not (0 <= row < len(board)) or not (0 <= col < len(board[0])) \
          or board[row][col] not in curr.next:
        return
      
      c = board[row][col]
      board[row][col] = '#'

      dfs(row + 1, col, curr.next[c])
      dfs(row - 1, col, curr.next[c])
      dfs(row, col + 1, curr.next[c])
      dfs(row, col - 1, curr.next[c])

      board[row][col] = c

    trie = Trie()
    for word in words:
      trie.insert(word)

    retval = []
    for i in range(len(board)):
      for j in range(len(board[0])):
        dfs(i, j, trie.root)
    
    return retval
# @lc code=end

