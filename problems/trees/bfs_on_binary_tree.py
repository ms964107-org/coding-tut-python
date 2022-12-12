"""
BFS on Binary Tree

簡單二元樹的廣度優先搜尋。深度優先搜尋在 Tree traversal 會討論到。

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
     1
    /  \
  2     2
   \     \
    3     3
Input: root = [1,2,2,null,3,null,3]
Output: [1,2,2,3,3]

來源：
程度：簡單
""" 
import sys
sys.path += ['../../utils/', '../../tests/trees']
from utils import TreeNode
from bfs_on_binary_tree_test import advanced_tests

# Tree 定義
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
    
def solution(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    # 你的程式碼寫在這
    import queue
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


    ###############

#####################################
"""
簡單測試
"""
q = TreeNode.build_tree([1,2,2,3,4,4,3], 0)
assert solution(q) == [1,2,2,3,4,4,3]
q = TreeNode.build_tree([1,2,2,None,3,None,3], 0)
assert solution(q) == [1,2,2,3,3]
print("BASIC TEST PASS")
advanced_tests(solution)
