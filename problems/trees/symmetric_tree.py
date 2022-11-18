"""
Symmetric tree

給予一個二元樹，請辨別他是否對稱。

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
Output: true

例子 2
     1
    /  \
  2     2
   \     \
    3     3
Input: root = [1,2,2,null,3,null,3]
Output: false

來源：https://leetcode.com/problems/symmetric-tree/
程度：簡單
""" 
import sys
sys.path += ['../../utils/', '../../tests/trees']
from utils import TreeNode
from symmetric_tree_test import advanced_tests

# Tree 定義
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
    
def solution(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    # 你的程式碼寫在這


    ###############

#####################################
"""
簡單測試
"""
q = TreeNode.build_tree([1,2,2,3,4,4,3], 0)
assert solution(q)
q = TreeNode.build_tree([1,2,2,None,3,None,3], 0)
assert not solution(q)
print("BASIC TEST PASS")
advanced_tests(solution)