#!/bin/python3

import sys
import math


def primes(n):  # simple Sieve of Eratosthenes
    odds = range(3, n+1, 2)
    sieve = set(sum([list(range(q*q, n+1, q+q)) for q in odds],[]))
    return [2] + [p for p in odds if p not in sieve]


def getHighestPrime(n):
    primeList = primes(n)
    if n in primeList:
        return n
    for k in reversed(range(2,(n//2)+1)):
        if n%k==0 and k in primeList:
            return k


def main():
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        print(getHighestPrime(n))


main()
