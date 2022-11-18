"""
Remove Duplicates from Sorted List

給予一個已照順序排列的 LinkedList，請刪除任何重複元素並回傳 LinkedList。

Constraints
一個 LinkedList 最少 0 Node 最多 50 Node
-100 <= Node.val <= 100
順序排列都是從小到大

例子
例子 1
Input: head = [1,1,2]
Output: [1,2]

例子 2
Input: head = [1,1,2,3,3]
Output: [1,2,3]

來源：https://leetcode.com/problems/remove-duplicates-from-sorted-list/
程度：簡單
"""
import sys
sys.path += ['../../utils/', '../../tests/linkedlists']
from utils import ListNode
from remove_duplicates_from_sorted_list_test import advanced_tests

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
    temp=head
    while temp:
        while temp.next!=None and temp.val == temp.next.val:
            temp.next=temp.next.next
        temp=temp.next
    return head

    ###############

#####################################
"""
簡單測試
"""
linkedlist = ListNode.list_to_linkedlist([1,1,2])
assert ListNode.linkedlist_to_list(solution(linkedlist)) == [1,2]
linkedlist = ListNode.list_to_linkedlist([1,1,2,3,3])
assert ListNode.linkedlist_to_list(solution(linkedlist)) == [1,2,3]
print("BASIC TEST PASS")
advanced_tests(solution)