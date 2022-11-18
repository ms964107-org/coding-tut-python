"""
Number of Islands

給予一個2D array grid做成的地圖，請判斷地圖中有幾個島嶼。島嶼的定義為陸地連接起來的區域。
2D array中，'1'為陸地，'0'為海。

Constraints
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'

例子 1
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

例子 2
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

來源：https://leetcode.com/problems/number-of-islands/
程度：中等
""" 
import sys
sys.path += ['../../tests/graphs']
from number_of_islands_test import advanced_tests
    
def solution(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    # 你的程式碼寫在這


    ###############

#####################################
"""
簡單測試
"""
grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]
assert solution(grid) == 1
grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
assert solution(grid) == 3
print("BASIC TEST PASS")
advanced_tests(solution)