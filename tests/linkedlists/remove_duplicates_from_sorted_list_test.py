import sys
sys.path += ['../../utils/']
from utils import ListNode, Test

def tests(solution):
    linkedlist = ListNode.list_to_linkedlist([1,1,2])
    assert ListNode.linkedlist_to_list(solution(linkedlist)) == [1,2]
    linkedlist = ListNode.list_to_linkedlist([1,1,2,3,3])
    assert ListNode.linkedlist_to_list(solution(linkedlist)) == [1,2,3]
    linkedlist = ListNode.list_to_linkedlist([1,1,2,3,4,4])
    assert ListNode.linkedlist_to_list(solution(linkedlist)) == [1,2,3,4]
    linkedlist = ListNode.list_to_linkedlist([1,1,2,3,4,4,4,4,4,4,4,4,4,5])
    assert ListNode.linkedlist_to_list(solution(linkedlist)) == [1,2,3,4,5]
    linkedlist = ListNode.list_to_linkedlist([])
    assert ListNode.linkedlist_to_list(solution(linkedlist)) == []
    linkedlist = ListNode.list_to_linkedlist([0])
    assert ListNode.linkedlist_to_list(solution(linkedlist)) == [0]
    linkedlist = ListNode.list_to_linkedlist([0,1])
    assert ListNode.linkedlist_to_list(solution(linkedlist)) == [0,1]
    linkedlist = ListNode.list_to_linkedlist([0,1,3])
    assert ListNode.linkedlist_to_list(solution(linkedlist)) == [0,1,3]
    linkedlist = ListNode.list_to_linkedlist([3,6,9,9,9,9])
    assert ListNode.linkedlist_to_list(solution(linkedlist)) == [3,6,9]
    linkedlist = ListNode.list_to_linkedlist([0,0,0,0,5,5,5,5,8,8,8])
    assert ListNode.linkedlist_to_list(solution(linkedlist)) == [0,5,8]
    linkedlist = ListNode.list_to_linkedlist([0,1,2])
    assert ListNode.linkedlist_to_list(solution(linkedlist)) == [0,1,2]
    linkedlist = ListNode.list_to_linkedlist([0,1,3])
    assert ListNode.linkedlist_to_list(solution(linkedlist)) == [0,1,3]
    linkedlist = ListNode.list_to_linkedlist([0,1,2,3,4,5,6])
    assert ListNode.linkedlist_to_list(solution(linkedlist)) == [0,1,2,3,4,5,6]
    linkedlist = ListNode.list_to_linkedlist([0,1,2,3,4,6,8])
    assert ListNode.linkedlist_to_list(solution(linkedlist)) == [0,1,2,3,4,6,8]
    linkedlist = ListNode.list_to_linkedlist([0,2,4,5])
    assert ListNode.linkedlist_to_list(solution(linkedlist)) == [0,2,4,5]
    linkedlist = ListNode.list_to_linkedlist([0,1,2,3])
    assert ListNode.linkedlist_to_list(solution(linkedlist)) == [0,1,2,3]
    linkedlist = ListNode.list_to_linkedlist([0,1,2,3,4,8,9])
    assert ListNode.linkedlist_to_list(solution(linkedlist)) == [0,1,2,3,4,8,9]
    linkedlist = ListNode.list_to_linkedlist([0,1,2,3,4,8,9,10,11,12,13])
    assert ListNode.linkedlist_to_list(solution(linkedlist)) == [0,1,2,3,4,8,9,10,11,12,13]
    linkedlist = ListNode.list_to_linkedlist([0,2,2,2,4,4,4,4,5,5,5,6])
    assert ListNode.linkedlist_to_list(solution(linkedlist)) == [0,2,4,5,6]
    linkedlist = ListNode.list_to_linkedlist([0,0,0,0,1,1,2,3,3,3,3])
    assert ListNode.linkedlist_to_list(solution(linkedlist)) == [0,1,2,3]
    linkedlist = ListNode.list_to_linkedlist([0,1,2,2,2,3,4,4,4,5,6])
    assert ListNode.linkedlist_to_list(solution(linkedlist)) == [0,1,2,3,4,5,6]
    linkedlist = ListNode.list_to_linkedlist([0,1,2,3,4,5,6,6,6,8])
    assert ListNode.linkedlist_to_list(solution(linkedlist)) == [0,1,2,3,4,5,6,8]
    linkedlist = ListNode.list_to_linkedlist([0,1,2,2,2,4,4,4,5,5,5,5])
    assert ListNode.linkedlist_to_list(solution(linkedlist)) == [0,1,2,4,5]
    linkedlist = ListNode.list_to_linkedlist([0,1,1,1,1,1,1,1,1,1,1,2,3,3,3,3,3,3])
    assert ListNode.linkedlist_to_list(solution(linkedlist)) == [0,1,2,3]

def advanced_tests(solution):
    Test.template(tests, solution)
