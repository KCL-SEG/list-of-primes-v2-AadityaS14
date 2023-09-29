"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

from math import sqrt

def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError(f"Number of primes should be a positive number.")
    list = []
    num = 2
    while len(list) < number_of_primes:
        if is_prime(num):
            list.append(num)
        num += 1
    return list

def is_prime(num):
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True