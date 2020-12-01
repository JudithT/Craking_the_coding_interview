

Class Node:
  def __init__(self,data):
      self.data = data
      self.next = None 
      
      
Class LL:
  def __init__():
      self.head = None
      
      
  def  remove_duplicate(self,head):
        counter = {}
        current = head
        while current: 
          if current in counter:
              current.next = current.next.next
          else:
              counter[current] = current 
              
              
   def remove_k_to_last(self,k):
        current = head 
        p1 = current
        while k > 0 :
            current = current.next 
            
        while current:
            current = current.next 
            p1 = p1.next 
        return p1
        
        
        
    def delete_middle_node(self):
        current = head 
        current = current.next
        current.next = current.next.next 
        
     # Part1   
    def palindrome(self):
        current = head 
        arr = []
        while current:
              arr.append(current.data)
              current = current.next 
        return arr == arr[::-1]
    
    #part2
    def palindrome(self,ll):
        slow = fast = ll.head
        stack = []
        while fast and fast.next:
            stack.append(slow.value)
            fast = fast.next.next
            slow = slow.next
       
        # this will take care of odds values
        if fast:
            slow = slow.next
            
        while slow:
            top = stack.pop()
            if top != slow.value:
                return False
            slow = slow.next
        return True 
        
                
   def Loop_detection(self):
        fast = head
        slow = head 
        
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
            
            if fast == slow : 
              return slow
                  
        return -1 
                
     # Part 1           
    def Intersection(self, l1, l2):
        Library = {}
        curr1 = l1
        curr2 = l2
        while curr1:
           library[curr1] = curr1
           curr1 = curr1.next 
           
        while curr2:
           if curr2 in library:
               return True
            else:
                library[curr2] = curr2
                
    # part 2
    
    def intersection(self, headA, headB):
        if not headA or not headB: return None
        p1 = headA
        p2 = headB
        
        while p1 and p2 and p1 != p2:
            p1 = p1.next 
            p2 = p2.next 
            if p1 == p2:
                return p1
            if not headA: p1 = headB
            if not headB: p2 = headA
                
        return p1
        
                
                
      def partition(self, ll, x):
          current = ll.tail = ll.head
          
          while current:
                nextNode = current.next
                current.next = None
                if current.value < x: 
                    current.next = ll.head
                    ll.head = current
                else:
                    ll.tail.next = current
                    ll.tail = current 
                current = nextNode
            if ll.tail.next is not None: 
                ll.tail.next = None 
            
    def sum_lists(self, l1, l2):
        
        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        tail = head = ListNode(0)
        carry = 0 
        first = l1.val
        second = l2.val
        carry, digit = divmod(carry  + first + second,10)
        tail.next = ListNode(digit)
        tail = tail.next
        l1 = l1.next 
        l2 = l2.next
        return head.next
    
        
        
        
        
        
          
            
        
#           
#           
#          
# 
#                 
#                 
#                 
#               
#               
# 
#         
# 
#       
