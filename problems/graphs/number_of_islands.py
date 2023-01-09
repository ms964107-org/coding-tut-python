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
    import queue
    class Node():
      def __init__(self,name):
        self.name = name
        self.visited = False
        self.neighbor = []
        self.count = 0

    q = queue.Queue()
    count = 0
    for column in range(0, len(grid)):
      for row in range(0, len(grid[column])):
        #print(int(grid[column[row]]))
        #root1 = grid[column][row] = TreeNode(object)
        #root1.val = grid[column][row]
        grid[column][row] = Node(name=None)
        if grid[column][row] == "0":
          continue
        #elif grid[column][row].visted != False:
        elif grid[column][row] == "1" and grid[column][row].visited == True:
          continue
        else:
          grid[column][row] = Node("1")
          if grid[column][row].name == "1" and grid[column][row].visited == True and grid[column][row].count == 0:
            count +=1
            print("array",column,row)
          grid[column][row].count = count
          grid[column][row].visited = True
          print("shit")

          def traversal(self):
            q.put(self)
            while q.qsize()>=0:
              print("run while")
              node = q.get(0) 
              print(q)
              if row +1 <= len(grid[column]):     #右
                grid[column][row+1] = Node("1")
                if grid[column][row+1] == "1" and grid[column][row+1].visited == False:   
                  grid[column][row+1].visited = True
                  grid[column][row+1].count = node.count
                  node.neighbor = rgrid[column][row+1]
                  q.append(grid[column][row+1])
                  print("right")
              if row -1 >= 0:     #左
                grid[column][row-1] = Node("1")
                if grid[column][row-1] == "1" and grid[column][row-1].visited == False:   
                  grid[column][row-1].visited = True
                  grid[column][row-1].count = node.count
                  node.neighbor = grid[column][row-1]
                  q.append(grid[column][row-1])
                  print("left")
              if column +1 <= len(grid):     #下
                grid[column+1][row] = Node("1")
                if grid[column+1][row] == "1" and grid[column+1][row].visited == False:   
                  grid[column+1][row].visited = True
                  grid[column+1][row].count = node.count
                  node.neighbor = grid[column+1][row]
                  q.append(grid[column+1][row])
                  print("down")
              if column -1 >= 0:     #上
                grid[column-1][row] = Node("1")
                if grid[column+1][row] == "1" and grid[column-1][row].visited == False:   
                  grid[column-1][row].visited = True
                  grid[column-1][row].count = node.count
                  node.neighbor = grid[column-1][row]
                  q.append(grid[column-1][row])
                  print("up")
          traversal(grid[column][row])
    print(count)
    return count
            

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