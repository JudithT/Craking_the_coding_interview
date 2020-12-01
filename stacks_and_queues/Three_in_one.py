# Describe how you could use a single array to implement three stacks. 

class ThreeStacks():
  def __init__(self):
    self.array = [None, None, None]
    self.current = [0, 1, 2] # initializing the  pointers for the stacks
#   stack 0 : 0,3,6,9
#   stack 1: 1,4,7,10
#   stack 2: 2,5,8,11
  def push(self, item, stack_number):
    if not stack_number in [0, 1, 2]:
      raise Exception("Bad stack number")
    while len(self.array) <= self.current[stack_number]: # To ensure that current[stack_number] is within bounds of array
      print("self.array",self.array)
      self.array += [None] * len(self.array) # doubling the length of the array
      print("self.array",self.array)
    self.array[self.current[stack_number]] = item
    self.current[stack_number] += 3
  
  def pop(self, stack_number):
    if not stack_number in [0, 1, 2]:
      raise Exception("Bad stack number")
    if self.current[stack_number] >= 3:
      self.current[stack_number] -= 3
    item = self.array[self.current[stack_number]]
    self.array[self.current[stack_number]] = None
    return item

import unittest

class Test(unittest.TestCase):
  def test_three_stacks(self):
    three_stacks = ThreeStacks()
    three_stacks.push(101, 0)
    three_stacks.push(102, 0)
    three_stacks.push(103, 0)
    three_stacks.push(201, 1)
    self.assertEqual(three_stacks.pop(0), 103)
    self.assertEqual(three_stacks.pop(1), 201)
    self.assertEqual(three_stacks.pop(1), None)
    self.assertEqual(three_stacks.pop(2), None)
    three_stacks.push(301, 2)
    three_stacks.push(302, 2)
    self.assertEqual(three_stacks.pop(2), 302)
    self.assertEqual(three_stacks.pop(2), 301)
    self.assertEqual(three_stacks.pop(2), None)

if __name__ == "__main__":
  unittest.main()