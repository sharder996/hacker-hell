#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:
  '''
  Accepted
  52/52 cases passed (224 ms)
  Your runtime beats 11.1 % of python3 submissions
  Your memory usage beats 76.12 % of python3 submissions (18.7 MB)

  Serialization:
  Time complexity : O(n)
  Space complexity : O(n)
  
  Deserialization:
  Time complexity : O(n)
  Space complexity : O(n)
  '''
  def serialize(self, root: TreeNode) -> str:
    """Encodes a tree to a single string.
    
    :type root: TreeNode
    :rtype: str
    """
    queue = [root]
    retval = []
    while queue:
      curr = queue.pop(0)
      if curr:
        retval.append(str(curr.val))
        queue.append(curr.left)
        queue.append(curr.right)
      else:
        retval.append('null')
    
    return '[' + ','.join(retval).strip('null,') + ']'

  def deserialize(self, data: str) -> TreeNode:
    """Decodes your encoded data to tree.
    
    :type data: str
    :rtype: TreeNode
    """
    if len(data) == 2:
      return None
    
    nodes = [None if val == 'null' else TreeNode(int(val)) for val in data.strip('[]').split(',')]
    stack = nodes[::-1]
    root = stack.pop()
    for node in nodes:
      if node:
        if stack:
          node.left = stack.pop()
        if stack:
          node.right = stack.pop()

    return root
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

