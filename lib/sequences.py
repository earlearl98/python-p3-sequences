#!/usr/bin/env python3

def print_fibonacci(length):

    fibonacci_sequence = [0, 1]

    for _ in range(2, length):
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    print(fibonacci_sequence[:length])


    