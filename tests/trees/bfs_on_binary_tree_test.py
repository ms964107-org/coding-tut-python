import sys
sys.path += ['../../utils/']
from utils import TreeNode, Test

def tests(solution):
  q = TreeNode.build_tree([1], 0)
  assert solution(q) == [1]
  q = TreeNode.build_tree([1,2,2], 0)
  assert solution(q) == [1,2,2]
  q = TreeNode.build_tree([1,None,2], 0)
  assert solution(q) == [1,2]
  q = TreeNode.build_tree([1,2,None], 0)
  assert solution(q) == [1,2]
  q = TreeNode.build_tree([1,2,2,3,None,None,3], 0)
  assert solution(q) == [1,2,2,3,3]
  q = TreeNode.build_tree([1,2,2,3,None,None,4], 0)
  assert solution(q) == [1,2,2,3,4]
  q = TreeNode.build_tree([1,2,2,None, 3, None, 3], 0)
  assert solution(q) == [1,2,2,3,3]
  q = TreeNode.build_tree([1,2,2,None, 3, None, 4], 0)
  assert solution(q) == [1,2,2,3,4]
  q = TreeNode.build_tree([1,2,2,3,5,5,3,4,None,None,None], 0)
  assert solution(q) == [1,2,2,3,5,5,3,4]
  q = TreeNode.build_tree([1,2,2,3,5,5,3,None,4,None,None], 0)
  assert solution(q) == [1,2,2,3,5,5,3,4]
  q = TreeNode.build_tree([1,2,2,3,5,5,3,None,None,4,None], 0)
  assert solution(q) == [1,2,2,3,5,5,3,4]
  q = TreeNode.build_tree([1,2,2,3,5,5,3,None,None,None,4], 0)
  assert solution(q) == [1,2,2,3,5,5,3,4]
  q = TreeNode.build_tree([1,2,2,3,5,5,3,None,4,None,4], 0)
  assert solution(q) == [1,2,2,3,5,5,3,4,4]
  q = TreeNode.build_tree([1,2,2,3,5,5,3,4,None,4,None], 0)
  assert solution(q) == [1,2,2,3,5,5,3,4,4]

def advanced_tests(solution):
    Test.template(tests, solution)
