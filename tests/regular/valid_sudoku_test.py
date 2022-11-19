import sys
sys.path += ['../../utils/']
from utils import Test

def tests(solution):
    assert solution(
        [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]])
    assert not solution(
        [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]])
    assert not solution(
        [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".","4","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]])
    assert not solution(
        [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".","7","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]])
    assert not solution(
        [["5","3",".",".","7",".",".",".","7"]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]])
    assert solution(
        [[".","7","2",".","1",".","5",".","."]
        ,[".","5",".","9",".",".",".","2","."]
        ,["3",".",".",".",".","2",".","8","."]
        ,["5",".",".",".","3",".","2",".","."]
        ,[".",".","1","5",".","9","3",".","."]
        ,[".",".","3",".","6",".",".",".","7"]
        ,[".","8",".","7",".",".",".",".","5"]
        ,[".","6",".",".",".","5",".","4","."]
        ,[".",".","5",".","4",".","8","7","."]])
    assert not solution(
        [[".","7","2",".","1",".","5",".","."]
        ,[".","5",".","9",".",".",".","2","."]
        ,["3",".",".",".",".","2",".","8","."]
        ,["5",".",".",".","3",".","2",".","."]
        ,[".",".","1","5",".","9","3",".","."]
        ,[".",".","3",".","6",".",".",".","7"]
        ,[".","8",".","7",".",".",".",".","5"]
        ,[".","6",".",".",".","5","4","4","."]
        ,[".",".","5",".","4",".","8","7","."]])
    assert not solution(
        [[".","7","2",".","1",".","5",".","."]
        ,[".","5",".","9",".",".",".","2","."]
        ,["3",".",".",".",".","2",".","8","."]
        ,["5",".",".",".","3",".","2",".","."]
        ,[".",".","1","5","1","9","3",".","."]
        ,[".",".","3",".","6",".",".",".","7"]
        ,[".","8",".","7",".",".",".",".","5"]
        ,[".","6",".",".",".","5",".","4","."]
        ,[".",".","5",".","4",".","8","7","."]])
    assert not solution(
        [[".","7","2",".","1",".","5",".","."]
        ,[".","5",".","9",".",".",".","2","."]
        ,["3",".",".",".",".","2",".","8","."]
        ,["5",".",".",".","3",".","2",".","."]
        ,[".",".","1","5",".","9","3",".","."]
        ,[".",".","3",".","6",".",".",".","7"]
        ,[".","8",".","7",".",".",".",".","5"]
        ,[".","6",".",".",".","5","3","4","."]
        ,[".",".","5",".","4",".","8","7","."]])
    assert not solution(
        [[".","7","2",".","1",".","5",".","."]
        ,[".","5",".","9",".",".",".","2","."]
        ,["3",".",".",".",".","2",".","8","."]
        ,["5",".",".",".","3",".","2",".","."]
        ,[".",".","1","5",".","9","3",".","."]
        ,[".",".","3",".","6",".",".",".","7"]
        ,[".","8",".","7","4",".",".",".","5"]
        ,[".","6",".",".",".","5",".","4","."]
        ,[".",".","5",".","4",".","8","7","."]])

def advanced_tests(solution):
    Test.template(tests, solution)