import sys
sys.path += ['../../utils/']
from utils import ListNode, Test

def tests(solution):
    list1 = ListNode.list_to_linkedlist([1,2,4])
    list2 = ListNode.list_to_linkedlist([1,3,4])
    assert ListNode.linkedlist_to_list(solution(list1, list2)) == [1,1,2,3,4,4]
    list1 = ListNode.list_to_linkedlist([1,2,4,4,4,4,4])
    list2 = ListNode.list_to_linkedlist([1,3,4,4,4,4,5])
    assert ListNode.linkedlist_to_list(solution(list1, list2)) == [1,1,2,3,4,4,4,4,4,4,4,4,4,5]
    list1 = ListNode.list_to_linkedlist([])
    list2 = ListNode.list_to_linkedlist([])
    assert ListNode.linkedlist_to_list(solution(list1, list2)) == []
    list1 = ListNode.list_to_linkedlist([])
    list2 = ListNode.list_to_linkedlist([0])
    assert ListNode.linkedlist_to_list(solution(list1, list2)) == [0]
    list1 = ListNode.list_to_linkedlist([])
    list2 = ListNode.list_to_linkedlist([0,1,2,3])
    assert ListNode.linkedlist_to_list(solution(list1, list2)) == [0,1,2,3]
    list1 = ListNode.list_to_linkedlist([])
    list2 = ListNode.list_to_linkedlist([0,2,4,5])
    assert ListNode.linkedlist_to_list(solution(list1, list2)) == [0,2,4,5]
    list1 = ListNode.list_to_linkedlist([1,3,6])
    list2 = ListNode.list_to_linkedlist([0,2,4,5])
    assert ListNode.linkedlist_to_list(solution(list1, list2)) == [0,1,2,3,4,5,6]
    list1 = ListNode.list_to_linkedlist([1,3,6])
    list2 = ListNode.list_to_linkedlist([0,2,4,8])
    assert ListNode.linkedlist_to_list(solution(list1, list2)) == [0,1,2,3,4,6,8]
    list1 = ListNode.list_to_linkedlist([1,3,9])
    list2 = ListNode.list_to_linkedlist([0,2,4,8])
    assert ListNode.linkedlist_to_list(solution(list1, list2)) == [0,1,2,3,4,8,9]
    list1 = ListNode.list_to_linkedlist([1,3,9,10,11,12,13])
    list2 = ListNode.list_to_linkedlist([0,2,4,8])
    assert ListNode.linkedlist_to_list(solution(list1, list2)) == [0,1,2,3,4,8,9,10,11,12,13]

def advanced_tests(solution):
    Test.template(tests, solution)
