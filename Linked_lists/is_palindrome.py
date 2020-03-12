class Node():
    
    def __init__(self,value):
        """ Initialiazing a node"""
        self.value = value
        self.next = None

class Linked_list:

    def __init__(self):
        """ Initializing the head of the Linked_list"""
        self.head = None

    def is_palindromecheck(self,string):
        return (string == string[::-1])


    def is_palindrome(self):
        node = self.head
        s = []
        while node is None: 
            s.append(s.data)
            node = node.next
            string = "".join(s)
        return self.is_palindromecheck(string)


    def printing_the_list(self):
        temp = self.head 
        while(temp):
            print(temp.data)
            temp = temp.next 

            

llist = Linked_list() 
llist.head = Node('a') 
llist.head.next = Node('bc') 
llist.head.next.next = Node("d") 
llist.head.next.next.next = Node("dcb") 
llist.head.next.next.next.next = Node("a") 
llist.is_palindrome 
print ("true") if llist.is_palindrome else ("false")




        


    




