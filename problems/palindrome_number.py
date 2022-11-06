"""
Palindrome Number

給予一個數字 "x"，請判斷是否為回文。
是請回傳 "True"，否則為 "False"。

Constraints
-2^31 <= x <= 2^31 - 1

例子 1
Input: x = 121
Output: true
Explanation: 往左念往右念都一樣

例子 2
Input: x = -121
Output: false

例子 3
Input: x = 10
Output: false

來源：https://leetcode.com/problems/palindrome-number/
程度：簡單
"""
def solution(x):
    """
    :type x: int
    :rtype: bool
    """
    # 你的程式碼寫在這


    ###############


#####################################
"""
簡單測試
"""
assert solution(121)
assert not solution(-121)
assert not solution(10)
print("BASIC TEST PASS")