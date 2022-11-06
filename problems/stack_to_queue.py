"""
Implementing Queue using Stack

請用兩個 stack 寫出一個 queue。
MyQueue類別有以函式：
    push(x) 放 "x" 到 queue 裡。
    pop(x) 從 queue 裡移出一個元素。
    peek(x) 看 queue 裡第一個元素。
    empty(x) 看 queue 裡是否有元素。空 queue 請回傳 "True"。

Constraints
0 <= x <= 9
你只能用 list.append() 和 list.pop()，且這兩者不能帶有變量
不能用 slice，比如說[:]
不能用 len()

例子
q = []
q.push(1) // q = [1]
q.push(2) // q = [1, 2]
q.push(3) // q = [1, 2, 3]
q.pop() // return 1, q = [2, 3]
q.peek() // return 2, q = [2, 3]
q.pop() // return 2, q = [3]
q.empty() // return False, q = [3]
q.pop() // return 3, q = []
q.empty() // return True, q = []

來源：https://leetcode.com/problems/implement-queue-using-stacks/
程度：簡單
"""
class MyQueue(object):
    def __init__(self):
        # 定義你的兩個stack


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

    def peek(self):
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
q = MyQueue()
q.push(1) # [1]
q.push(2) # [1, 2]
q.push(3) # [1, 2, 3]
assert q.pop() == 1 # [2, 3]
assert q.peek() == 2
assert q.pop() == 2 # [3]
assert not q.empty()
assert q.pop() == 3 # []
assert q.empty()
assert q.pop() is None
assert q.peek() is None
print("BASIC TEST PASS")