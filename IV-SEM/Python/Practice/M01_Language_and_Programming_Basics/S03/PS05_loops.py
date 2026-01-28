# while loop
'''counter = 0
while counter < 5:
    print("Hello world!")
    counter += 1

n = int(input())
counter = 0
while n > 0:
    n = n // 10
    counter += 1
print(counter)'''

#for loop
'''for i in range(0, 5, 1):
    print("Hello world!")'''

# list = [1, 2, 3, 4, 5]
# for i in range(len(list)):
#     list[i] = list[i] ** 2
# print(list)

# for i in range(len(list)):
#     if list[i] % 2 == 0:
#         print(list[i], end = " ")

# for element in list:
#     if element % 2 == 0:
#         print(element, end = " ")

# string = input() 
# count = 0
# for ch in string:
#     if ch in"aeiouAEIOU":
#         count += 1
# print(count)

# for i in range(1, 11):
#     if i == 5:
#         continue
#     print (i, end = " ")

password = "Chaitu@123"
p = input("Enter the password: ")
if p == password:
    print("login successful")
else: 
    for i in range(3):
        p = input("Enter the password: ")
        if i == 3 and p != password:
            print("account locked")
            break