import sys
sys.path.append('../problems/')
from remove_duplicates_from_sorted_list import solution

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
linkedlist = list_to_linkedlist([1,1,2])
assert linkedlist_to_list(solution(linkedlist)) == [1,2]
linkedlist = list_to_linkedlist([1,1,2,3,3])
assert linkedlist_to_list(solution(linkedlist)) == [1,2,3]
linkedlist = list_to_linkedlist([1,1,2,3,4,4])
assert linkedlist_to_list(solution(linkedlist)) == [1,2,3,4]
linkedlist = list_to_linkedlist([1,1,2,3,4,4,4,4,4,4,4,4,4,5])
assert linkedlist_to_list(solution(linkedlist)) == [1,2,3,4,5]
linkedlist = list_to_linkedlist([])
assert linkedlist_to_list(solution(linkedlist)) == []
linkedlist = list_to_linkedlist([0])
assert linkedlist_to_list(solution(linkedlist)) == [0]
linkedlist = list_to_linkedlist([0,1])
assert linkedlist_to_list(solution(linkedlist)) == [0,1]
linkedlist = list_to_linkedlist([0,1,3])
assert linkedlist_to_list(solution(linkedlist)) == [0,1,3]
linkedlist = list_to_linkedlist([3,6,9,9,9,9])
assert linkedlist_to_list(solution(linkedlist)) == [3,6,9]
linkedlist = list_to_linkedlist([0,0,0,0,5,5,5,5,8,8,8])
assert linkedlist_to_list(solution(linkedlist)) == [0,5,8]
linkedlist = list_to_linkedlist([0,1,2])
assert linkedlist_to_list(solution(linkedlist)) == [0,1,2]
linkedlist = list_to_linkedlist([0,1,3])
assert linkedlist_to_list(solution(linkedlist)) == [0,1,3]
linkedlist = list_to_linkedlist([0,1,2,3,4,5,6])
assert linkedlist_to_list(solution(linkedlist)) == [0,1,2,3,4,5,6]
linkedlist = list_to_linkedlist([0,1,2,3,4,6,8])
assert linkedlist_to_list(solution(linkedlist)) == [0,1,2,3,4,6,8]
linkedlist = list_to_linkedlist([0,2,4,5])
assert linkedlist_to_list(solution(linkedlist)) == [0,2,4,5]
linkedlist = list_to_linkedlist([0,1,2,3])
assert linkedlist_to_list(solution(linkedlist)) == [0,1,2,3]
linkedlist = list_to_linkedlist([0,1,2,3,4,8,9])
assert linkedlist_to_list(solution(linkedlist)) == [0,1,2,3,4,8,9]
linkedlist = list_to_linkedlist([0,1,2,3,4,8,9,10,11,12,13])
assert linkedlist_to_list(solution(linkedlist)) == [0,1,2,3,4,8,9,10,11,12,13]
linkedlist = list_to_linkedlist([0,2,2,2,4,4,4,4,5,5,5,6])
assert linkedlist_to_list(solution(linkedlist)) == [0,2,4,5,6]
linkedlist = list_to_linkedlist([0,0,0,0,1,1,2,3,3,3,3])
assert linkedlist_to_list(solution(linkedlist)) == [0,1,2,3]
linkedlist = list_to_linkedlist([0,1,2,2,2,3,4,4,4,5,6])
assert linkedlist_to_list(solution(linkedlist)) == [0,1,2,4,5,6]
linkedlist = list_to_linkedlist([0,1,2,3,4,5,6,6,6,8])
assert linkedlist_to_list(solution(linkedlist)) == [0,1,2,3,4,5,6,8]
linkedlist = list_to_linkedlist([0,1,2,2,2,4,4,4,5,5,5,5])
assert linkedlist_to_list(solution(linkedlist)) == [0,1,2,4,5]
linkedlist = list_to_linkedlist([0,1,1,1,1,1,1,1,1,1,1,2,3,3,3,3,3,3])
assert linkedlist_to_list(solution(linkedlist)) == [0,1,2,3]
# done
print("ADVANCED TEST PASS")