import sys
sys.path += ['../../utils/']
from utils import Test

def tests(solution):
    grid = [
        ["1","1","1","1","1"],
        ["1","1","1","1","1"],
        ["1","1","1","1","1"],
        ["1","1","1","1","1"]
    ]
    assert solution(grid) == 1
    grid = [
        ["0","0","0","0","0"],
        ["0","0","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","0","0"]
    ]
    assert solution(grid) == 1
    grid = [
        ["0","1","0","0","0"],
        ["1","0","1","1","0"],
        ["0","1","1","0","0"],
        ["0","0","0","0","1"]
    ]
    assert solution(grid) == 4
    grid = [
        ["1","1","0","1","0"],
        ["1","0","0","1","0"],
        ["1","0","1","0","1"],
        ["0","0","0","1","1"]
    ]
    assert solution(grid) == 4
    grid = [
        ["1","1","1","1","0"],
        ["1","0","0","1","1"],
        ["0","0","1","0","1"],
        ["1","0","1","0","1"]
    ]
    assert solution(grid) == 3
    grid = [
        ["0","0","1","1","0"],
        ["0","1","1","1","1"],
        ["1","0","1","0","0"],
        ["1","0","1","0","0"]
    ]
    assert solution(grid) == 2
    grid = [
        ["0","1","0","1","1"],
        ["1","0","1","0","0"],
        ["1","0","0","1","1"],
        ["0","1","0","1","1"]
    ]
    assert solution(grid) == 6
    grid = [
        ["0","0","0","1","1"],
        ["0","1","1","0","0"],
        ["1","0","0","0","1"],
        ["1","1","0","1","1"]
    ]
    assert solution(grid) == 4

def advanced_tests(solution):
    Test.template(tests, solution)
