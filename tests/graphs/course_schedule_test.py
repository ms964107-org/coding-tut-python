import sys
sys.path += ['../../utils/']
from utils import Test

def tests(solution):
    assert solution(2, [[1,0]])
    assert not solution(2, [[1,0],[0,1]])
    assert solution(4, [[1,0],[2,3]])
    assert not solution(3, [[0,1],[1,2],[2,0]])
    assert solution(6, [[0,1],[0,2],[3,5],[5,4]])
    assert solution(6, [[0,1],[0,2],[3,5],[5,4],[2,4]])
    assert solution(6, [[0,1],[0,2],[3,5],[5,4],[2,3]])
    assert not solution(6, [[0,1],[0,2],[3,5],[5,4],[2,3],[4,0]])
    assert not solution(6, [[0,1],[0,2],[4,0],[3,5],[5,4],[2,3]])
    assert solution(5, [[0,1],[0,2],[0,3],[2,4]])
    assert solution(4, [[0,1],[0,2],[0,3]])
    assert solution(4, [[0,1],[0,2],[0,3],[2,3]])
    assert solution(4, [[0,1],[3,2],[0,2],[0,3]])
    assert solution(5, [[0,1],[3,2],[0,2],[0,3],[4,0]])
    assert not solution(5, [[0,1],[3,2],[0,2],[0,3],[4,0],[3,0]])

def advanced_tests(solution):
    Test.template(tests, solution)
