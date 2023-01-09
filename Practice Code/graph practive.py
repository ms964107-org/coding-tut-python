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

import queue
list1 = ["1","1","0","1","0","1","1"]
class solution:
  def numisland(self, list:list[str]) ->int:
    count = 0
    visited = set()

    def dfs(r):
      if(
        r in visited or
        r < 0 or r > len(list)-1 or
        list[r] == "0"
        ):
        return
      else:
        visited.add(r)
        dfs(r+1)
        dfs(r-1)

    for r in range(len(list)):
      if list[r] == "1" and not r in visited:
        dfs(r)
        count += 1
      else:
        continue
    return count


q = solution()
print(q.numisland(list1))
  
    


