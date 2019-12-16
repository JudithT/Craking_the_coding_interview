""" 
Given two singly linked lists, determine if the two lists intersect. Return the intersection node.
Note that the intersection is defined based on the reference,not value. That is, if teh kth node of 
the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting """


def intersecting(LL1,LL2):
    if LL1.tail != LL2.tail:
        return False 
    longer_list = LL1 if len(LL1) > len(LL2) else LL2
    shortter_list = LL2 if len(LL2) < len(LL1) else LL1 

    diff = len(LL1) - len(LL2)
    shorter_node = shortter_list.head
    longer_node = longer_list.head

    for i in range(diff):
        longer_node.next

    while longer_node != shorter_node:
          longer_node.next 
          shorter_node.next 

    return longer_node
