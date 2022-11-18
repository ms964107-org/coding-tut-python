import sys
sys.path += ['../../utils/']
from utils import ListNode, Test

def tests(solution):
    assert solution(ListNode.list_to_linkedlist_with_cycle([3,2,0,-4], 0))
    assert solution(ListNode.list_to_linkedlist_with_cycle([1,2,7,3,8,3,9,6,3], 5))
    assert not solution(ListNode.list_to_linkedlist_with_cycle([1,2,3,4], None))
    assert solution(ListNode.list_to_linkedlist_with_cycle([3,2,0,-4], 1))
    assert solution(ListNode.list_to_linkedlist_with_cycle([1,2,3,8,3,9,2], 3))
    assert not solution(ListNode.list_to_linkedlist_with_cycle([1,2,4,1,5,3,3,4], None))
    assert solution(ListNode.list_to_linkedlist_with_cycle([3,2,0,-4], 2))
    assert solution(ListNode.list_to_linkedlist_with_cycle([1,3,3,8,3,9,2], 1))
    assert not solution(ListNode.list_to_linkedlist_with_cycle([1,8,5,9,3,2,3,4], None))
    assert solution(ListNode.list_to_linkedlist_with_cycle([3,2,0,-4,6,7,8], 3))
    assert solution(ListNode.list_to_linkedlist_with_cycle([9,3,8,3,9,1,2], 5))
    assert not solution(ListNode.list_to_linkedlist_with_cycle([1,2,4,7,9,1,2,6,9,3,4], None))
    assert solution(ListNode.list_to_linkedlist_with_cycle([3,2,0,-4,7,2,1,3,3,3,3,7], 8))
    assert solution(ListNode.list_to_linkedlist_with_cycle([1,3,3,8,3,9,2,9,2,6,3], 4))

def advanced_tests(solution):
    Test.template(tests, solution)
