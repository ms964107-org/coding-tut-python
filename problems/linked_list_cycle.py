"""
Linked List Cycle

給予一個 LinkedList，判斷是否有迴圈。

Constraints
一個 LinkedList 最少 0 Node 最多 50 Node
-100 <= Node.val <= 100

例子
例子 1
Input: head = [3,2,0,-4]
3 -> 2 -> 0 -> -4 --
     ^             |
     |_____________|
                   
Output: true

例子 2
Input: head = [1,2]
1 -> 2 --
^        |
|________|

Output: true

例子 2
Input: head = [1,2,3,4]
1 -> 2 -> 3 -> 4
Output: false

來源：https://leetcode.com/problems/linked-list-cycle/
程度：簡單
"""
import sys
sys.path.append('../utils/')
from utils import ListNode

# Node 定義
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def solution(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    # 你的程式碼寫在這


    ###############

#####################################
"""
簡單測試
"""
assert solution(ListNode.list_to_linkedlist_with_cycle([3,2,0,-4], 1))
assert solution(ListNode.list_to_linkedlist_with_cycle([1,2], 0))
assert not solution(ListNode.list_to_linkedlist_with_cycle([1,2,3,4], None))
print("BASIC TEST PASS")