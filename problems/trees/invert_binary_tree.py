"""
Invert binary tree

給予一個二元樹，請把它反轉。

Constraints
0 <= Node.val <= 100
Number of nodes [1,1000]

例子 1
     1
    /  \
  2     2
 / \   / \
3   4 4   3
Input: root = [1,2,2,3,4,4,3]
Output: [1,2,2,3,4,4,3]

例子 2
     4                  4
   /   \              /   \
  2     7     <->    7     2
 / \   / \          / \   / \
1   3 6   9        9   6 3   1
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

例子 3
     2              2
   /   \   <->    /   \
  1     3        3     1
Input: root = [2,1,3]
Output: [2,3,1]

例子 4
Input: root = []
Output: []

來源：https://leetcode.com/problems/invert-binary-tree/
程度：簡單
""" 
import sys
sys.path += ['../../utils/', '../../tests/trees']
from utils import TreeNode
from invert_binary_tree_test import advanced_tests

# Tree 定義
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
    
def solution(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    # 你的程式碼寫在這


    ###############

#####################################
"""
簡單測試
"""
t = TreeNode.build_tree([1,2,2,3,4,4,3], 0)
assert TreeNode.isSameTree(solution(t), t)
t1 = TreeNode.build_tree([4,2,7,1,3,6,9], 0)
t2 = TreeNode.build_tree([4,7,2,9,6,3,1], 0)
assert TreeNode.isSameTree(solution(t1), t2)
t1 = TreeNode.build_tree([2,1,3], 0)
t2 = TreeNode.build_tree([2,3,1], 0)
assert TreeNode.isSameTree(solution(t1), t2)
t1 = TreeNode.build_tree([], 0)
t2 = TreeNode.build_tree([], 0)
assert TreeNode.isSameTree(solution(t1), t2)
print("BASIC TEST PASS")
advanced_tests(solution)