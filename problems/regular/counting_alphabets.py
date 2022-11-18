"""
Counting Alphabets

給予一個文字串 "s" ，請回傳此字串裡出現最多次的字母。

Constraints
1 <= s.length <= 100
"s" 只有大小寫英文字母和空白' '
大小寫字母是不同的字母
如果有兩個以上出現最多次的字母，任意回傳一個即可

例子 1
Input: s = "Hello World"
Output: 'l'
Explanation: 出現最多次的是 "l"，3次

例子 2
Input: s = "   fly me   to   the moon  "
Output: 'o'

例子 3
Input: s = "luffy is still joyboy"
Output: 'l'

來源：https://leetcode.com/problems/majority-element/
程度：簡單
"""
import sys
sys.path += ['../../tests/regular']
from counting_alphabets_test import advanced_tests

def solution(s):
    """
    :type s: str
    :rtype: str
    """
    # 你的程式碼寫在這


    ###############


#####################################
"""
簡單測試
"""
assert solution("Hello World") == 'l'
assert solution("   fly me   to   the moon  ") == 'o'
assert solution("luffy is still joyboy") == 'l'
print("BASIC TEST PASS")
advanced_tests(solution)