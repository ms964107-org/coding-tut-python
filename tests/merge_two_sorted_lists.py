import sys
sys.path.append('../problems/')
from merge_two_sorted_lists import solution

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

# test cases
list1 = list_to_linkedlist([1,2,4])
list2 = list_to_linkedlist([1,3,4])
assert linkedlist_to_list(solution(list1, list2)) == [1,1,2,3,4,4]
list1 = list_to_linkedlist([1,2,4,4,4,4,4])
list2 = list_to_linkedlist([1,3,4,4,4,4,5])
assert linkedlist_to_list(solution(list1, list2)) == [1,1,2,3,4,4,4,4,4,4,4,4,4,5]
list1 = list_to_linkedlist([])
list2 = list_to_linkedlist([])
assert linkedlist_to_list(solution(list1, list2)) == []
list1 = list_to_linkedlist([])
list2 = list_to_linkedlist([0])
assert linkedlist_to_list(solution(list1, list2)) == [0]
list1 = list_to_linkedlist([])
list2 = list_to_linkedlist([0,1,2,3])
assert linkedlist_to_list(solution(list1, list2)) == [0,1,2,3]
list1 = list_to_linkedlist([])
list2 = list_to_linkedlist([0,2,4,5])
assert linkedlist_to_list(solution(list1, list2)) == [0,2,4,5]
list1 = list_to_linkedlist([1,3,6])
list2 = list_to_linkedlist([0,2,4,5])
assert linkedlist_to_list(solution(list1, list2)) == [0,1,2,3,4,5,6]
list1 = list_to_linkedlist([1,3,6])
list2 = list_to_linkedlist([0,2,4,8])
assert linkedlist_to_list(solution(list1, list2)) == [0,1,2,3,4,6,8]
list1 = list_to_linkedlist([1,3,9])
list2 = list_to_linkedlist([0,2,4,8])
assert linkedlist_to_list(solution(list1, list2)) == [0,1,2,3,4,8,9]
list1 = list_to_linkedlist([1,3,9,10,11,12,13])
list2 = list_to_linkedlist([0,2,4,8])
assert linkedlist_to_list(solution(list1, list2)) == [0,1,2,3,4,8,9,10,11,12,13]
# done
print("ADVANCED TEST PASS")