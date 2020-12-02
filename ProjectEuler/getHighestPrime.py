#!/bin/python3

import numpy

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def primesn(n):
    """ Returns a array of primes, 3 <= p < n """
    sieve = numpy.ones(n//2, dtype=numpy.bool)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = False
    return 2*numpy.nonzero(sieve)[0][1::]+1


def main():
    k = 0
    presents = 0
    for i in range(0, 5433000):
        if k > 0:
            k -=  1
            continue
        if '7' in str(i):
            k += max(primes(i))
            continue
        presents += 1

    print(presents)

main()
