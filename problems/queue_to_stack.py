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
q = []
q.push(1) // q = [1]
q.push(2) // q = [1, 2]
q.push(3) // q = [1, 2, 3]
q.pop() // return 3, q = [1, 2]
q.top() // return 2, q = [1, 2]
q.pop() // return 2, q = [1]
q.empty() // return False, q = [1]
q.pop() // return 1, q = []
q.empty() // return True, q = []

來源：https://leetcode.com/problems/implement-stack-using-queues/
程度：簡單
"""
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
q = MyStack()
q.push(1) # [1]
q.push(2) # [1, 2]
q.push(3) # [1, 2, 3]
assert q.pop() == 3 # [1, 2]
assert q.top() == 2
assert q.pop() == 2 # [1]
assert not q.empty()
assert q.pop() == 1 # []
assert q.empty()
assert q.pop() is None
assert q.top() is None
print("BASIC TEST PASS")
