'''
1. Write code for factorial of a number
2. Write code to check whether a number is armstrong or not
3. Write code to check whether a number is prime or not
4. Write code to check whether a list of numbers is monotomic or not
5. print reverse of a number
6. given a roman numeral, convert it to an integer
7. Happy Number
'''
'''#1. Write code for factorial of a number
n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"The factorial of {n} is {factorial}")'''

'''#2. Write code to check whether a number is armstrong or not
n = int(input("Enter a number: "))
order = len(str(n))
sum = 0
temp = n
while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10
if n == sum:
    print(f"{n} is an armstrong number")
else:    
    print(f"{n} is not an armstrong number")'''

'''#3. Write code to check whether a number is prime or not
n = int(input("Enter a number: "))
if n > 1:   
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"{n} is not a prime number")
            break
    else:
        print(f"{n} is a prime number")'''

'''#4. Write code to check whether a list of numbers is monotomic or not
arr = list(map(int, input("Enter a list of numbers: ").split()))
inc = True
dec = True
for i in range(1, len(arr)-1):
    if arr[i] > arr[i + 1]:
        dec = False
    elif arr[i] < arr[i + 1]:
        inc = False
    if inc or dec:
        print("The list is monotomic")
    else:       
        print("The list is not monotomic")'''

'''#5. print reverse of a number
n = int(input("Enter a number: "))
reverse = 0
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n //= 10
print(f"The reverse of the number is {reverse}")
#32-bit signed integer range
if reverse < -2**31 or reverse > 2**31 - 1:
    print(0)
else:   
    print(f"The reverse of the number is {reverse}")'''

'''#6. given a roman numeral, convert it to an integer
s = input("Enter a roman numeral: ").upper()
roman_numerals = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
total = 0
prev_value = 0
for char in s:
    value = roman_numerals[char]
    if prev_value < value:
        total += value - 2 * prev_value
    else:
        total += value
    prev_value = value
print(f"The integer value of the roman numeral is {total}")'''

#7. Happy Number
n = int(input("Enter a number: "))
def is_happy(num):
    seen = set()
    while num != 1 and num not in seen:
        seen.add(num)
        num = sum(int(digit) ** 2 for digit in str(num))
    return num == 1
if is_happy(n):
    print(f"{n} is a happy number")
else:    
    print(f"{n} is not a happy number")

