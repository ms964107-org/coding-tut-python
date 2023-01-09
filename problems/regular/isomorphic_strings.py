"""
Isomorphic Strings

給予兩個字串 "s" 和 "t"，請判斷他們是否為 isomorphic。
Isomorphic 的定義是 "s" 字串裡的各個字母可以對應到 "t" 裡的各個字母。
字串 "s" 各個字母不會同時對應到的 "t" 的同個字母。

Constraints
1 <= s.length <= 100
1 <= t.length <= 100
"s" 和 "t" 不會有空格

例子 1
Input: s = "egg", t = "add"
Output: true
Explanation: "e" maps to "a", "g" maps to "d".

例子 2
Input: s = "foo", t = "bar"
Output: false

例子 3
Input: s = "paper", t = "title"
Output: true

來源：https://leetcode.com/problems/isomorphic-strings/
程度：簡單
"""
import sys
sys.path += ['../../tests/regular']
from isomorphic_strings_test import advanced_tests

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
assert solution("add", "egg")
assert not solution("foo", "bar")
assert solution("paper", "title")
print("BASIC TEST PASS")
advanced_tests(solution)