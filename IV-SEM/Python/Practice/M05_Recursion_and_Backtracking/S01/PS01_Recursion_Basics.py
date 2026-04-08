'''
#Sum of N natural numbers
def Natural_Sum(n):
    s = 0
    for i in range(1, n+1):
        s += i
    return s
print(Natural_Sum(5)) 
print(Natural_Sum(10))

#Using Recursion
def Natural_Sum(n):
    if n == 1:
        return 1
    else:
        return n + Natural_Sum(n-1)

print(Natural_Sum(5))
print(Natural_Sum(10))

#Factorial of a Number In Traditional Way
def Factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

print(Factorial(5))
print(Factorial(10))

#Factorial of a Number using Recursion
def Factorial(n):
    if n < 0:
        return "Factorial doesnot exist for -ve numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * Factorial(n-1)
    
print(Factorial(5))
print(Factorial(10))

#Fibbonacci Series in Traditional Way
def Fibonacci(n):
    if n <= 0:
        return n
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)
print(Fibonacci(5))
#Fibbonacci Series using Recursion
def Fibonacci1(n):
    if n <= 0:
        return n
    elif n == 1:
        return 0
    elif n == 2:
        return 1   
    else:
        return Fibonacci1(n - 1) + Fibonacci1(n - 2)
print(Fibonacci1(7))

#GCD of two numbers in Traditional Way
def GCD(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a
print(GCD(48, 18))
print(GCD(56, 98))
'''
#GCD of two numbers using Recursion
def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)
print(GCD(48, 18))
print(GCD(56, 98))