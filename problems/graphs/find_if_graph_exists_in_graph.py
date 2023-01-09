"""
Find if Path Exists in Graph

給予一個包含各個邊的 list "edges" 和代表點的數量的 "n" 和兩個點的位置：起點 "source" 和終點 "destination"，請判斷起點和終點之間有沒有路徑。

Constraints
1 <= n <= 10
0 <= edges.length <= 10
edges[i].length == 2
0 <= ui, vi <= n - 1
ui != vi
0 <= source, destination <= n - 1
沒有重複的邊。
沒有指向自己的邊。
邊是雙向的。

例子 1
0 - 1
 \ /
  2
Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2

例子 2
  1       3
 /       |  \
0 - 2    4 - 5
Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.

來源：https://leetcode.com/problems/find-if-path-exists-in-graph/
程度：簡單
""" 
import sys
sys.path += ['../../tests/graphs']
from find_if_graph_exists_in_graph_test import advanced_tests
    
def solution(n, edges, source, destination):
    """
    :type n: int
    :type edges: List[List[int]]
    :type source: int
    :type destination: int
    :rtype: bool
    """
    # 你的程式碼寫在這


    ###############

#####################################
"""
簡單測試
"""
assert solution(3, [[0,1],[1,2],[2,0]], 0, 2)
assert not solution(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5)
print("BASIC TEST PASS")
advanced_tests(solution)