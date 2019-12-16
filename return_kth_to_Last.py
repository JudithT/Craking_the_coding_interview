""" 
        Implement an algorithm to find the kth elemenet of a singly linked list 
  """

# from LinkedList import LinkedList
from collections import deque

def k_to_last(ll, k ):
    current = runner = ll.head
    while k > 0:
        if  runner is None:
            return None
        runner = runner.next

    while(runner):
           current = current.next
           runner = runner.next 

    return current 


ll = LinkedList()
ll.generate(10, 0, 99)
print(ll)
print(kth_to_last(ll, 3))
