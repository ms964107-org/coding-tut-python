"""
Valid Parentheses

給予一個只含有各種括號的字串 "s"，請判斷此字串各個括號是否都有對應的括號。

Constraints
括號包含 (), [], {}
1 <= s.length <= 10^4

例子 1
Input: s = "()"
Output: True

例子 2
Input: s = "()[]{}"
Output: True

例子 3
Input: s = "(]"
Output: False
Explanation: "(" and "]" are not closed by the same type of brackets

例子 4
Input: s = "([{}])"
Output: True

例子 5
Input: s = "[(])"
Output: False
Explanation: "(" and "]" are not closed by the same type of brackets

來源：https://leetcode.com/problems/valid-parentheses/
程度：簡單
"""
def solution(s):
    """
    :type s: str
    :rtype: bool
    """
    # 你的程式碼寫在這


    ###############


#####################################
"""
簡單測試
"""
assert solution("()")
assert solution("()[]{}")
assert not solution("(]")
assert solution("([{}])")
assert not solution("[(])")
print("BASIC TEST PASS")