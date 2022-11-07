# LinkedList
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

# Tree
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def build_tree(list, index):
        parent = None
        if index < len(list):
            if list[index] == None:
                return
            parent = TreeNode(list[index])
            parent.left = TreeNode.build_tree(list, 2 * index + 1)
            parent.right = TreeNode.build_tree(list, 2 * index + 2)
        return parent
