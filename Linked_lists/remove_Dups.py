""" 
Write a code to remove duplicates from an unsorted linked list 

Follow UP

How would you solve this problem if a temporary buffer is not allowed
"""


class Node(object):
   """ Node in a linked list """
   def __init__(self,data):
       self.data = data 
       self.next = None 



class LinkedList(object):
    """ Linked List """
    def __init__(self):
        self.head = None


    def remove_duplicate(self):

        if self.head is None: 
            return 

        seen = set()

       current = self.head

       while (current.next):
           if current.data in seen:
               current.next = current.next.next 
            else:
                seen.add(current.data)

            current =  current.next 

        return head 



