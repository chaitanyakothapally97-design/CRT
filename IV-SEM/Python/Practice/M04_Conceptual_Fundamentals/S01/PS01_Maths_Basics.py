'''
Maths Basics in Python:
1. Basic Arithmetic Operators(+, -, *, /, //, %, **)
2. Important built-in math functions (abs(), round(), min(), max(), sum(), pow()
3. Math functions from math module (math.sqrt(), math.factorial(), math.ceil(), math.floor(), math.pi)
'''
'''#1. Basic Arithmetic Operators
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

#2. Important built-in math functions
print(abs(-96))
print(round(3.14159))
print(min([10, 20, 30, 40, 50]))
print(max([10, 20, 30, 40, 50]))
print(sum([10, 20, 30, 40, 50]))
print(pow(9, 6))

#3. Math functions from math module
import math
print(math.sqrt(96))
print(math.ceil(4.2))
print(math.floor(4.8))
print(math.pi)
print(math.factorial(5))

#A. Find the GCD of two numbers
import math
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(math.gcd(a, b))

#B. Find the LCM of two numbers
import math
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(math.lcm(a, b))

#C. Find whether the number is a perfect number or not
n = int(input("Enter a number: "))
sum_of_divisors = 0
for i in range(1, n):
    if n % i == 0:
        sum_of_divisors += i
if sum_of_divisors == n:
    print("The number is a perfect number.")
else:
    print("The number is not a perfect number.")


#LeetCode Problem:412. Fizz Buzz
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result
        '''
#LeetCode Problem:1822. Sign of the Product of an Array
from ast import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for num in nums:
            product *= num
        if product > 0:
            return 1
        elif product < 0:
            return -1
        else:
            return 0
        
