import sys
sys.path += ['../../utils/']
from utils import TreeNode, Test

def tests(solution):
    t1 = TreeNode.build_tree([1,2,4,None,3,None,3], 0)
    t2 = TreeNode.build_tree([1,4,2,3,None,3,None], 0)
    assert TreeNode.isSameTree(solution(t1), t2)
    t = TreeNode.build_tree([1], 0)
    assert TreeNode.isSameTree(solution(t), t)
    t = TreeNode.build_tree([1,2,2], 0)
    assert TreeNode.isSameTree(solution(t), t)
    t1 = TreeNode.build_tree([1,None,2], 0)
    t2 = TreeNode.build_tree([1,2,None], 0)
    assert TreeNode.isSameTree(solution(t1), t2)
    t1 = TreeNode.build_tree([1,2,None], 0)
    t2 = TreeNode.build_tree([1,None,2], 0)
    assert TreeNode.isSameTree(solution(t1), t2)
    t = TreeNode.build_tree([1,2,4,3,None,None,3], 0)
    assert TreeNode.isSameTree(solution(t), t)
    t1 = TreeNode.build_tree([1,2,2,3,None,None,4], 0)
    t2 = TreeNode.build_tree([1,2,2,4,None,None,3], 0)
    assert TreeNode.isSameTree(solution(t1), t2)
    t1 = TreeNode.build_tree([1,2,5,None, 3, None, 4], 0)
    t2 = TreeNode.build_tree([1,5,2,4,None,3,None], 0)
    assert TreeNode.isSameTree(solution(t1), t2)

def advanced_tests(solution):
    Test.template(tests, solution)
