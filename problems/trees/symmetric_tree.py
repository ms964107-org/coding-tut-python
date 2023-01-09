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
    import queue
    def bfs(r):
      q = queue.Queue()
      result = []
      q.put(r)
      while q.qsize() >0:
            node = q.get()
            result.append(node.val)
            if node.left != None:
                  q.put(node.left)
            if node.right != None:
                  q.put(node.right)
      return result
    # 你的程式碼寫在這
    list1 = []
    curr = root
    def inorderleft (root, list1):
        if root != None:
            if root.left != None:
                inorderleft(root.left, list1)
            list1.append(root.val)
            if root.right != None:
                inorderleft(root.right, list1)
    inorderleft(root, list1)

    r = list1.index(curr.val)
    list11 = []
    for i in range(0, r):
      list11.append(list1[i])

    list2 = []
    def travelsal (root, list2):    #inorderright
        if root != None:
            if root.right != None:
                travelsal(root.right, list2)
            list2.append(root.val)
            if root.left != None:
                travelsal(root.left, list2)
    travelsal(root, list2)
    
    list22 = []
    r = list1.index(curr.val)
    for l in range(0, r):
      list22.append(list2[l])


    #Check
    print("list11",list11)
    for a in list11:
      print("type:", a,type(a))
    print("list22",list22)
    for b in list22:
      print("type:", b,type(b))

    if list11 == list22:
      return True
    return False
    
    



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




"""
import queue
def bfs(r):
      q = queue.Queue()
      result = []
      q.put(r)
      while q.qsize() >0:
            node = q.get()
            result.append(node.val)
            if node.left != None:
                  q.put(node.left)
            if node.right != None:
                  q.put(node.right)
      return result
"""
