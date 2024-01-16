#!/usr/bin/env python3

def print_fibonacci(length):
    fib_sequence = []

    if length == 0:
        print(fib_sequence)
        return

    if length == 1:
        fib_sequence.append(0)
        print(fib_sequence)
        return

    if length == 2:
        fib_sequence.extend([0, 1])
        print(fib_sequence)
        return

    fib_sequence = [0, 1]

    for i in range(2, length):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    print(fib_sequence)

# Test cases
print_fibonacci(0)
print_fibonacci(1)
print_fibonacci(2)
print_fibonacci(10)



 
        
        
        
