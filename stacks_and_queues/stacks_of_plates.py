class Stack_of_plates:
    def __init__(self, capacity):
        self.stack = [] # array of stacks 
        if capacity < 1:
            raise NameError("A stack is greater than one ")
        else:
            self.capacity = capacity

    def push(self, item):
        if self.stack == [] or len(self.stack[-1]) >= capacity:
            self.stack.append([item])
        else:
            self.stack[-1].append(item)

    def pop(self):
        if self.stack ==[]:
            raise NameError("Cannot pop from an empty stack")
        poppedData = self.stack[-1][-1]
        if len(self.stack[-1][-1]) == 1:
            del self.stack[-1]
        else:
            del self.stack[-1][-1]

        return poppedData

    def popAtindex(self, index):
        if self.stack == []
            raise NameError("We cannot pop from an empty stack")
        if index  > len(self.stack) - 1: # make sure that index falls between the stack range that we have. 
            raise NameError("Index is out of range")
        else:
            poppedData = self.stack[index][-1]
            if len(self.stack[index] == 1): # if stack has only one element at the moment
                del self.stack[-1]
            elif len(self.stack[index]) == index:
                del self.stack[index][-1]
        return poppedData


Stack of plates: Imagine a (literal) stack of plates. if the stack gets too high, it might topple.Therefire , in real life we would likely
start a new stack when the previous stack exceeds some threshold.Implement a data structure SetOfStacks that mimics this. SetOfStacks should 
be composed of several stacks and should create a new stack once the previous one exceeds capacity. Set(that is pop() should return 
the same values as it would if there were just single stack)

Folow up 
Implement a function (int index) which performs a pop operation on a soecific sub-stack 



