"""
Valid Anagram

給予兩個單詞 "s" 和 "t"，請判斷他們是否為 Anagram。
Anagram 定義為由一個單詞之間各個字母排列組合成另一個單詞。

Constraints
1 <= s.length <= 10^4
1 <= t.length <= 10^4
大小寫字母是不同的字母

例子 1
Input: s = "anagram", t = "nagaram"
Output: true

例子 2
Input: s = "rat", t = "car"
Output: false

例子 3
Input: s = "iamlordvoldemort", t = "tommarvoloriddle"
Output: true

來源：https://leetcode.com/problems/valid-anagram/
程度：簡單
"""
import sys
sys.path += ['../../tests/regular']
from valid_anagram_test import advanced_tests

def solution(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    # 你的程式碼寫在這


    ###############


#####################################
"""
簡單測試
"""
assert solution("anagram", "nagaram")
assert not solution("rat", "car")
assert solution("iamlordvoldemort", "tommarvoloriddle")
print("BASIC TEST PASS")
advanced_tests(solution)