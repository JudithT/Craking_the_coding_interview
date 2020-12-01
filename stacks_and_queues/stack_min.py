class StackMin:
    def __init__(self):
        self.stack = []

    def add(self, item):
        minval = self.getmin()
        minval = min(minval, item)
        self.stack.append((item, minval))

    def getmin():
        if len(self.stack) == 0:
            return inf("float")
        return self.stack[-1][1]

    def remove(self):
        data = self.stack.pop()
        return data 

add(5) - mini = 5 
add(1) - mini = 1
add(1000) - mini= 1
Stack min :
How would you design a stack which, in addition to push and pop, has function min which returns the minimun element? 
Push, pop and minimun element? Push, pop and min should all operate in 0(1) time 