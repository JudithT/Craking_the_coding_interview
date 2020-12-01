def Sorting_a_stack(input_stack):
    sorted_stack = []
    while(len(input_stack)) != 0 : 
        next_value_to_sort = input_stack.pop()
        while(len(sorted_stack) != 0 ) and sorted_stack[-1] > next_value_to_sort:
            input_stack.append(sorted_stack.pop())
        sorted_stack.append(next_value_to_sort)
    return sorted_stack


print(Sorting_a_stack([100,2,300,1000,0,-1]))


# write a program to sort a stack such that the smallest items are on the top. You can use an additional temporay stack, but you may want 
#ot copy the elements into any other data structures (such as an array). The stack supports the following operations: Push, pop, IsEmpty
