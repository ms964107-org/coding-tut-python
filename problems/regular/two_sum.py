"""
Two Sum

給予一個陣列 "nums" 和一個整數 "target"，請回傳當兩個數字之和等於 "target" 時，這兩個數字在陣列裡的位置。
如果找不到該 "target"，請回傳 -1。

Constraints
2 <= nums.length <= 10^4
只有一個答案

例子 1
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, return [0, 1]

例子 2
Input: nums = [3,3], target = 6
Output: [0,1]

例子 3
Input: nums = [4,6], target = 7
Output: -1

來源：https://leetcode.com/problems/two-sum/
程度：簡單
"""
import sys
sys.path += ['../../tests/regular']
from two_sum_test import advanced_tests

def solution(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int, int
    """
    # 你的程式碼寫在這


    ###############


#####################################
"""
簡單測試
"""
a, b = solution([2,7,11,15], 9)
assert a == 0 and b == 1
a, b = solution([3,3], 6)
assert a == 0 and b == 1
assert solution([4,6], 7) == -1
print("BASIC TEST PASS")
advanced_tests(solution)