class QueueViaStacks:
    def__init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()
    
    def add(self,item):
        self.in_stack.append(item)

    def remove(self):
        if len(self.out_stack) == 0:
            while(len(self.in_stack)):
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()

    class Stack():
        def __init__(self):
            self.array = []

        def __len__(self):
            return len(self.array)

        def push(self, item):
            self.array.append(item)

        def pop(self):
            if not len(self.array):
                return None
            return self.array.pop()


# Implement a MyQueue class which implements a queue using two stacks         