"""
Backspace String Compare

給予兩個字串 "s" 和 "t"，字串裡只有小寫字母和 "#"，代表退格。請判斷此兩字串是否相同。

Constraints
0 <= s.length <= 10^4
0 <= t.length <= 10^4
"s" 和 "t" 只含小寫字母和 "#"

例子 1
Input: s = "ab#c", t = "ad#c"
Output: True
Explanation: Both s and t become "ac".

例子 2
Input: s = "ab##", t = "c#d#"
Output: True
Explanation: Both s and t become "".

例子 3
Input: s = "a#c", t = "b"
Output: False
Explanation: s becomes "c" while t becomes "b".

來源：https://leetcode.com/problems/backspace-string-compare/
程度：簡單
"""
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
assert solution("ab#c", "ab#c")
assert solution("ab##", "c#d#")
assert not solution("a#c", "b")
print("BASIC TEST PASS")