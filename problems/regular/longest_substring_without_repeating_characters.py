"""
Longest Substring Without Repeating Characters

給予一個字串 "s"，請找出最長的不含重複字母的子字串的長度。

Constraints
0 <= s.length <= 20
"s" 只有英文字母

例子 1
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

例子 2
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

例子 3
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

來源：https://leetcode.com/problems/longest-substring-without-repeating-characters/
程度：中等
"""
import sys
sys.path += ['../../tests/regular']
from longest_substring_without_repeating_characters_test import advanced_tests

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
assert solution("abcabcbb") == 3
assert solution("bbbbb") == 1
assert solution("pwwkew") == 3
print("BASIC TEST PASS")
advanced_tests(solution)