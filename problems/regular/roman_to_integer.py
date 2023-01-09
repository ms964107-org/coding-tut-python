"""
Roman to Integer

請把羅馬數字 "s" 轉成阿拉伯數字。

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

注意 4 是 "IV" 而不是 "IIII"，9也是同理，是 "IX"。
相對的，只要有數字4或9，都得做相應的變化。
比如說 40 是 "XL"，90 是 "XC"。

Constraints
羅馬數字為 [1,3999]

例子 1
Input: s = "III"
Output: 3
Explanation: III = 3.

例子 2
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

例子 3
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

來源：https://leetcode.com/problems/roman-to-integer/
程度：簡單
"""
import sys
sys.path += ['../../tests/regular']
from roman_to_integer_test import advanced_tests

def solution(s):
    """
    :type s: str
    :rtype: int
    """
    # 你的程式碼寫在這


    ###############


#####################################
"""
簡單測試
"""
assert solution("III") == 3
assert solution("LVIII") == 58
assert solution("MCMXCIV") == 1994
print("BASIC TEST PASS")
advanced_tests(solution)