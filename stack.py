"""
Implementation of a stack

LIFO

push()
pop()
size()
peek()
"""


class Stack:
    def __init__(self):
        self.stack_representation = []
    

    def push(self, value):
        self.stack_representation.append(value)
    

    def pop(self):
        ret_val = self.stack_representation[-1]
        del self.stack_representation[-1]
        print(ret_val)

    
    def __str__(self):
        return ', '.join(map(str, self.stack_representation))


my_stack = Stack()

my_stack.push(5)
my_stack.push(3)
my_stack.push(6)
my_stack.push(7)
my_stack.pop()
print(my_stack)