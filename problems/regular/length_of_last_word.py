"""
Length of Last Word

給予一個文字串 "s" ，請回傳此字串裡最後一個單字的長度。

Constraints
1 <= s.length <= 100
"s" 只有英文字母和空白' '
"s" 裡至少會有一個單字

例子 1
Input: s = "Hello World"
Output: 5
Explanation: 最後一個字是 "World" 長度是 5

例子 2
Input: s = "   fly me   to   the moon  "
Output: 4

例子 3
Input: s = "luffy is still joyboy"
Output: 6

來源：https://leetcode.com/problems/length-of-last-word/
程度：簡單
"""
import sys
sys.path += ['../../tests/regular']
from length_of_last_word_test import advanced_tests

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
assert solution("Hello World") == 5
assert solution("   fly me   to   the moon  ") == 4
assert solution("luffy is still joyboy") == 6
print("BASIC TEST PASS")
advanced_tests(solution)