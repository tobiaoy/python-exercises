"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    #return -1
    if position < 0:
        return -1
    elif position == 0:
        return 0
    elif position == 1:
        return 1
    else:
        num = get_fib(position - 1) + get_fib(position - 2)
        return num

# Test cases
print(get_fib(9))
print(get_fib(11))
print(get_fib(0))
# print(get_fib(50))