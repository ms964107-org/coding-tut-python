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
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
    
def solution(t1, t2):
    """
    :type root1: TreeNode
    :type root2: TreeNode
    :rtype: TreeNode
    """
    # 你的程式碼寫在這
      list1 = []
      list2 = []
      list3 = []
      curr = t1
      def travelsal (t1, list1):
            if t1 != None:
                  if t1.left != None:
                        travelsal(t1.left, list1)
                        list1.append(root.val)
                  if root.right != None:
                        travelsal(t1t.right, list1)
            travelsal(t1, list1)
           
      def travelsal2 (t2, list2):
            num = 0
            if t2 != None:
                  if t2.left != None:
                        travelsal2(t2.left, list2)
                        list2.append(t2.val+list1[num])
                        num+=1
                  if root.right != None:
                        travelsal2(t2.right, list2)
            travelsal(t2, list2)
      return list2
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
