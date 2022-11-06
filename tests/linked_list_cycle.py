import sys
sys.path.append('../problems/')
from remove_duplicates_from_sorted_list import solution

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_linkedlist_with_cycle(list, pos):
    head = curr = ListNode()
    loop = None
    for i, e in enumerate(list):
        curr.next = ListNode(e)
        curr = curr.next
        if (i == pos):
            loop = curr
    curr.next = loop
    return head.next

# test cases
assert solution(list_to_linkedlist_with_cycle([3,2,0,-4], 0))
assert solution(list_to_linkedlist_with_cycle([1,2,7,3,8,3,9,6,3], 5))
assert not solution(list_to_linkedlist_with_cycle([1,2,3,4], None))
assert solution(list_to_linkedlist_with_cycle([3,2,0,-4], 1))
assert solution(list_to_linkedlist_with_cycle([1,2,3,8,3,9,2], 3))
assert not solution(list_to_linkedlist_with_cycle([1,2,4,1,5,3,3,4], None))
assert solution(list_to_linkedlist_with_cycle([3,2,0,-4], 2))
assert solution(list_to_linkedlist_with_cycle([1,3,3,8,3,9,2], 1))
assert not solution(list_to_linkedlist_with_cycle([1,8,5,9,3,2,3,4], None))
assert solution(list_to_linkedlist_with_cycle([3,2,0,-4,6,7,8], 3))
assert solution(list_to_linkedlist_with_cycle([9,3,8,3,9,1,2], 5))
assert not solution(list_to_linkedlist_with_cycle([1,2,4,7,9,1,2,6,9,3,4], None))
assert solution(list_to_linkedlist_with_cycle([3,2,0,-4,7,2,1,3,3,3,3,7], 8))
assert solution(list_to_linkedlist_with_cycle([1,3,3,8,3,9,2,9,2,6,3], 4))
# done
print("ADVANCED TEST PASS")