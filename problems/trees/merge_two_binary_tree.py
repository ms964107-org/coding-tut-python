"""
Merge Two Binary Tree

給予兩個二元樹，請合併並回傳。

Constraints
0 <= Node.val <= 100
Number of nodes [1,1000]

例子 1
      1            2              3
    /  \         /  \            /  \
  3     2   +   1    3    =     4    5
 /               \    \        / \    \
5                 4    7      5   4    7
Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]

例子 2
   1        1         2
      +    /    =    /
          2         2
Input: root1 = [1], root2 = [1,2]
Output: [2,2]

來源：https://leetcode.com/problems/merge-two-binary-trees/
程度：簡單
""" 
import sys
sys.path += ['../../utils/', '../../tests/trees']
from utils import TreeNode
from merge_two_binary_tree_test import advanced_tests

# Tree 定義
#class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
    
def solution(t1, t2):
      r1 = t1
      r2 = t2
      r3 = TreeNode(object)
      r3.val = r1.val + r2.val
      def traversal(r1,r2,r3):
            if r1.left != None or r2.left != None:
                  r3.left = TreeNode(object)
                  if r1.left == None:
                        r1.left = TreeNode(object)
                        r3.left.val = r2.left.val
                  elif r2.left == None:
                        r2.left = TreeNode(object)
                        r3.left.val = r1.left.val
                  elif r1.left != None and r2.left != None:
                        r3.left.val = r1.left.val + r2.left.val
                  traversal(r1.left, r2.left, r3.left)
            if r1.right != None or r2.right != None:
                  r3.right = TreeNode(object)
                  if r1.right == None:
                        r1.right = TreeNode(object)
                        r3.right.val = r2.right.val
                  elif r2.right ==  None:
                        r2.right = TreeNode(object)
                        r3.right.val = t1.right.val
                  elif r1.right != None and r2.right != None:
                        r3.right.val = r1.right.val + r2.right.val
                  traversal(r1.right, r2.right, r3.right)
      traversal(r1,r2,r3)

      import queue
      def bfs(root):
            q = queue.Queue()
            result = []
            q.put(root)
            while q.qsize() >0:
                  node = q.get()
                  result.append(node.val)
                  if node.left != None:
                        q.put(node.left)
                  if node.right != None:
                        q.put(node.right)
            return result
      print("r1",bfs(r1))
      print("r2",bfs(r2))
      print("r3",bfs(r3))    
      return r3

    ###############

#####################################
"""
簡單測試
"""
t1 = TreeNode.build_tree([1,3,2,5],0)
t2 = TreeNode.build_tree([2,1,3,None,4,None,7],0)
r = TreeNode.build_tree([3,4,5,5,4,None,7],0)
assert TreeNode.isSameTree(solution(t1, t2),r)
t1 = TreeNode.build_tree([1],0)
t2 = TreeNode.build_tree([1,2],0)
r = TreeNode.build_tree([2,2],0)
assert TreeNode.isSameTree(solution(t1, t2),r)
print("BASIC TEST PASS")
advanced_tests(solution)
