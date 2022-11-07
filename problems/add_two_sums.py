"""
Add Two Sums

給予兩個非空白的 LinkedList，每一個 LinkedList 代表一個數字，而每一個 node 含一個個位數字。
比如說 LinkedList: 1 -> 2 -> 3 -> 4 代表數字 1234。
請把這兩個非空白的 LinkedList 加起來並回傳一個代表此總和的 LinkedList。

Constraints
1 <= LinkedList.length <= 100
0 <= Node.val <= 9

例子 1
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

例子 2
Input: l1 = [0], l2 = [0]
Output: [0]

例子 3
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

來源：https://leetcode.com/problems/add-two-numbers/
程度：中等
"""
import sys
sys.path.append('../utils/')
from utils import ListNode

# Node 定義
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def solution(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    # 你的程式碼寫在這


    ###############


#####################################
"""
簡單測試
"""
linedlist1 = ListNode.list_to_linkedlist([2,4,3])
linedlist2 = ListNode.list_to_linkedlist([5,6,4])
assert ListNode.linkedlist_to_list(solution(linedlist1, linedlist2)) == [7,0,8]
linedlist1 = ListNode.list_to_linkedlist([0])
linedlist2 = ListNode.list_to_linkedlist([0])
assert ListNode.linkedlist_to_list(solution(linedlist1, linedlist2)) == [0]
linedlist1 = ListNode.list_to_linkedlist([9,9,9,9,9,9,9])
linedlist2 = ListNode.list_to_linkedlist([9,9,9,9])
assert ListNode.linkedlist_to_list(solution(linedlist1, linedlist2)) == [8,9,9,9,0,0,0,1]
print("BASIC TEST PASS")