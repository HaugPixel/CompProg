# Simple Fibonacci

def Fibonacci(n):
    a = 0
    b = 1
    while n:
        print(a+b, end=" ")
        tempA = a
        a = b
        b = tempA + b
        n-=1


def sumEvenFibonacci(n):
    a = 0
    b = 2
    summ = 0
    while b<n:
        summ += b
        b, a = b*4 + a, b




    return summ

print(sumEvenFibonacci(100))