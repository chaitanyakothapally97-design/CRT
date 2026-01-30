# Number Series: 
'''
1. Print n natural numbers:
2. print n even numbers:
3. print n odd numbers:
4. print n Fibonacci series:
5. print tables:
6. print squares of n natural numbers:
7. print cubes of n natural numbers:
8. print alternative series:
    a) 1, -2, 3, -4, 5, -6 .....
    b) -1, 2, -3, 4, -5, 6 .....
    c) 1, 2, 4, 7, 11, 16, .....
    d) 1, 2, 6, 24, 120, ......

'''
#1. Print n natural numbers
'''n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print(i, end = " ")'''

#2. print n even numbers
'''n = int(input("Enter a number: "))
for i in range(2, n + 1, +2):
    print(i, end = " ")'''

# 3. print n odd numbers
'''n = int(input("Enter a number: "))
for i in range(1, n + 1, +2):
    print(i, end = " ")'''

# 4. print n Fibonacci series
'''n = int(input("Enter a number: ")) 
a, b = 0, 1
for i in range(n):
    print(a, end = " ")
    a, b = b, a + b

#Using while loop
n = int(input("Enter a number: "))      
a, b = 0, 1
i = 0      
while i < n:
    print(a, end = " ")
    a, b = b, a + b
    i += 1'''

#5. print tables
'''n = int(input("Enter a nuber: "))
for i in range(1, 21, +1):
    print(f"{n} x {i} = {n*i}")

#Using while loop
n = int(input("Enter a nuber: "))       
i = 1      
while i <= 20:
    print(f"{n} x {i} = {n*i}")
    i += 1'''

#6. print squares of n natural numbers
'''n = int(input("Enter a number: "))      
for i in range(1, n + 1):
    print(i ** 2, end = " ")
print()

#Using while loop
n = int(input("Enter a number: "))      
i = 1      
while i <= n:   
    print(i ** 2, end = " ")
    i += 1  '''

#7. print cubes of n natural numbers
'''n = int(input("Enter a number: "))      
for i in range(1, n + 1):
    print(i ** 3, end = " ")
print()

#Using while loop
n = int(input("Enter a number: "))  
i = 1
while i <= n:   
    print(i ** 3, end = " ")
    i += 1 ''' 

#8. print alternative series:
#a) 1, -2, 3, -4, 5, -6 .....
'''n = int(input("Enter a number: "))      
for i in range(1, n + 1, +1):
    if i % 2 != 0:
        print(i, end = " ")
    else:
        print(-i , end = " ")'''

#b) -1, 2, -3, 4, -5, 6 .....
'''n = int(input("Enter a number: "))
for i in range(1, n + 1, +1):
    if i % 2 == 0:
        print(i , end = " ")   
    else:
        print(-i, end = " ")'''

#c) 1, 2, 4, 7, 11, 16, .....
'''n = int(input("Enter a number: "))  
a = 1
diff = 0 
for i in range(n):
    print(a, end = " ")
    diff += 1
    a += diff'''

#d) 1, 2, 6, 24, 120, .....
'''n = int(input("Enter a number: "))
a = 1
increment = 1
for i in range(n):
    print(a, end = " ")
    increment += 1
    a *= increment'''

# Using while loop
n = int(input("Enter a number: "))
a = 1
increment = 1
i = 0
while i < n:    
    print(a, end = " ")
    increment += 1
    a *= increment
    i += 1