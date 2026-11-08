# my first python module/package(idk the difference).
'''has two functions: isprime() and areprimes(). isprime() works with one number and areprimes() works with multiple numbers.'''
import math
def isprime(n):
    ''' only works with one number. returns "True" or "False" based on whether the number is prime or not respectively.'''
    if n < 2:
        return False
    if n in (2, 3):
        return True
    limit = math.isqrt(n) + 1
    for i in range(5, limit, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def areprimes(*args):
    ''' works with multiple numbers. returns "True" or "False" based on whether all the numbers are prime or not respectively.'''
    for n in args:
        if not isprime(n):
            return False
    return True

def primes_till_that_num(n):
    ''' returns all prime numbers smaller than n, in a list called "primes_till_that_num".'''
    if n < 3:
        return []
    primes_till_that_num = []
    for i in range(2, n):
        if isprime(i):
            primes_till_that_num.append(i)
    return primes_till_that_num

def that_many_primes(n):
    ''' returns the first n prime numbers, in a list called "that_many_primes".'''
    if n < 1:
        return []
    that_many_primes = []
    i = 2
    while len(that_many_primes) < n:
        if isprime(i):
            that_many_primes.append(i)
        i += 1
    return that_many_primes