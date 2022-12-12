"""
DFS on Binary Tree: Tree Traversal

給予一個二元樹，請完成這些深度優先搜尋：前序遍歷、中序遍歷、後序遍歷。

Constraints
0 <= Node.val <= 100

例子 1
     1
    /  \
  2     3
   \   / \
    4  5  6
Input: root = [1,2,3,None,4,5,6]
Output: pre order traversal: [1, 2, 4, 3, 5, 6]
        in order traversal: [2, 4, 1, 5, 3, 6]
        post order traversal: [4, 2, 5, 6, 3, 1]

來源：https://leetcode.com/problems/binary-tree-inorder-traversal/
程度：簡單
"""
import sys
sys.path += ['../../utils/', '../../tests/trees']
from utils import TreeNode
from dfs_on_binary_tree_test import advanced_tests

# Tree 定義
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
        
def pre_order_traversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    # 你的程式碼寫在這

    list1 = []
    def travelsal (root, list1):
        if root != None:
            list1.append(root.val)
            if root.left != None:
                travelsal(root.left, list1)
            if root.right != None:
                travelsal(root.right, list1)
    travelsal(root, list1)
    return list1


    ###############
    
def in_order_traversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    # 你的程式碼寫在這
    # 往左dfs
    list1 = []
    def travelsal (root, list1):
        if root != None:
            if root.left != None:
                travelsal(root.left, list1)
            list1.append(root.val)
            if root.right != None:
                travelsal(root.right, list1)
    travelsal(root, list1)
    return list1



    ###############
 
def post_order_traversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    # 你的程式碼寫在這
    list1 = []
    def travelsal (root, list1):
        if root != None:
            if root.left != None:
                travelsal(root.left, list1)
            if root.right != None:
                travelsal(root.right, list1)
            list1.append(root.val)
    travelsal(root, list1)
    return list1


    ###############


#####################################
"""
簡單測試
"""
q = TreeNode.build_tree([1,2,3,None,4,5,6], 0)
assert pre_order_traversal(q) == [1, 2, 4, 3, 5, 6]
assert in_order_traversal(q) == [2, 4, 1, 5, 3, 6]
assert post_order_traversal(q) == [4, 2, 5, 6, 3, 1]
q = TreeNode.build_tree([1, 2, 3, 4, 5, None, 6], 0)
assert pre_order_traversal(q) == [1, 2, 4, 5, 3, 6]
assert in_order_traversal(q) == [4, 2, 5, 1, 3, 6]
assert post_order_traversal(q) == [4, 5, 2, 6, 3, 1]
q = TreeNode.build_tree([4, 6, 2, None, 5, 1, 9, 2, 1, 3, 4, None, 7], 0)
assert pre_order_traversal(q) == [4, 6, 5, 3, 4, 2, 1, 7, 9]
assert in_order_traversal(q) == [6, 3, 5, 4, 4, 1, 7, 2, 9]
assert post_order_traversal(q) == [3, 4, 5, 6, 7, 1, 9, 2, 4]
print("BASIC TEST PASS")
advanced_tests([pre_order_traversal, in_order_traversal, post_order_traversal])