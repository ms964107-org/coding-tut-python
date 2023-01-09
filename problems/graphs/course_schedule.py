"""
Course schedule

你需要拿 "numCourses" 門課才能畢業，而 "prerequisites" 代表你的課表之間課程的先後順序。
比如說，prerequisites = [a, b]，代表你在拿 b 課之前得先把 a 課修過。
請根據你的課表，請判斷你是否能畢業。

Constraints
1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses

例子 1
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

例子 2
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

來源：https://leetcode.com/problems/course-schedule/
程度：中等
""" 
import sys
sys.path += ['../../tests/graphs']
from course_schedule_test import advanced_tests
    
def solution(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    # 你的程式碼寫在這


    ###############

#####################################
"""
簡單測試
"""
assert solution(2, [[1,0]])
assert not solution(2, [[1,0],[0,1]])
print("BASIC TEST PASS")
advanced_tests(solution)