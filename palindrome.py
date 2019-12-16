

def is_LL_a_palindrome(self):
    """ First approach: Make use of a stack, First loop to collect data and store in a stack. Second loop to compare the value in the loop with the popped value  """
    s = []
    p = self.head

    while p:
        s.append(p.data)
        p = p.next

    while p:
        data = s.pop()
        if data != p.data:
            return False
        p = p.next 
    return True 


def is_LL_a_palindrome(self)
""" loop through the list and collect values as a string. compare the string value and its reverse"""
     p = self.head
     s = ""
    while p: 
        s += p.data 
        p = p.next
    return s == s[::-1]

     

