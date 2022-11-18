"""
Implementing Stack using Queue

請用兩個 queue 寫出一個 stack
MyStack類別有以函式：
    push(x) 放 "x" 到 stack 裡。
    pop(x) 從 stack 裡移出一個元素。
    top(x) 看 stack 裡第一個元素。
    empty(x) 看 stack 裡是否有元素。空 stack 請回傳 "True"。

Constraints
0 <= x <= 9
你只能用 list.append() 和 list.pop(0)，list.append() 不能帶有變量
不能用 slice，比如說[:]
不能用 len()

例子
s = []
s.push(1) // s = [1]
s.push(2) // s = [1, 2]
s.push(3) // s = [1, 2, 3]
s.pop() // return 3, s = [1, 2]
s.top() // return 2, s = [1, 2]
s.pop() // return 2, s = [1]
s.empty() // return False, s = [1]
s.pop() // return 1, s = []
s.empty() // return True, s = []

來源：https://leetcode.com/problems/implement-stack-using-queues/
程度：簡單
"""
import sys
sys.path += ['../../tests/regular']
from queue_to_stack_test import advanced_tests

class MyStack(object):
    def __init__(self):
        # 定義你的兩個queue

    # 你的程式碼寫在這，完成以下函式
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """

    def pop(self):
        """
        :rtype: int
        :rtype: None, if empty
        """

    def top(self):
        """
        :rtype: int
        :rtype: None, if empty
        """

    def empty(self):
        """
        :rtype: bool
        """  


#####################################
"""
簡單測試
"""
s = MyStack()
s.push(1) # [1]
s.push(2) # [1, 2]
s.push(3) # [1, 2, 3]
assert s.pop() == 3 # [1, 2]
assert s.top() == 2
assert s.pop() == 2 # [1]
assert not s.empty()
assert s.pop() == 1 # []
assert s.empty()
assert s.pop() is None
assert s.top() is None
print("BASIC TEST PASS")
advanced_tests(MyStack())
