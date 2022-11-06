"""
Merge Two Sorted Lists

請把兩個已照順序排列的 LinkedList 合併成一個有照順序排列的 LinkedList。

Constraints
一個 LinkedList 最少 0 Node 最多 50 Node
-100 <= Node.val <= 100
順序排列都是從小到大

例子
例子 1
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

例子 2
Input: list1 = [], list2 = []
Output: []

例子 3
Input: list1 = [], list2 = [0]
Output: [0]

來源：https://leetcode.com/problems/merge-two-sorted-lists/
程度：簡單
"""

# Node 定義
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solution(list1, list2):
    """
    :type list1: Optional[ListNode]
    :type list2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """


#####################################
"""
簡單測試
"""
def list_to_linkedlist(list):
    head = curr = ListNode()
    for e in list:
        curr.next = ListNode(e)
        curr = curr.next
    return head.next

def linkedlist_to_list(linkedlist):
    list = []
    while linkedlist:
        list.append(linkedlist.val)
        linkedlist = linkedlist.next
    return list

linedlist1 = list_to_linkedlist([1,2,4])
linedlist2 = list_to_linkedlist([1,3,4])
assert linkedlist_to_list(solution(linedlist1, linedlist2)) == [1,1,2,3,4,4]
linedlist1 = list_to_linkedlist([])
linedlist2 = list_to_linkedlist([])
assert linkedlist_to_list(solution(linedlist1, linedlist2)) == []
linedlist1 = list_to_linkedlist([])
linedlist2 = list_to_linkedlist([0])
assert linkedlist_to_list(solution(linedlist1, linedlist2)) == [0]
print("BASIC TEST PASS")