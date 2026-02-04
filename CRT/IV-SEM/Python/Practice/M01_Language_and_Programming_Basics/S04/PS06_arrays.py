'''
Arrays:
1. List ==> built-in Data Structure
    1. Use [] to create a list
    2. list is heterogeneous
    3. list is mutable
    4. List is indexed
    5. List is ordered
    6. List allows duplicate values

2. Array using array module
3. Array using numpy module
'''
# #1. List
# li = [1, 12.5, True, 7 + 9j, "Chaitu"]
# print(li, type(li))

# #No.of elements len()
# print(len(li))

# #Update 
# li[2] = False
# print(li)

# #Adding element ==> append()
# li.append("Sindhu")
# print(li)

# #Inserting element ==> insert(index, value)
# li.insert(5, "Met")
# print(li)

# li.insert(-20, 200)
# print(li)

# li.insert(20, 97)
# print(li)

# #Extend ==> to add multiple elements
# li.extend([100, 200, 300])
# print(li)

# #Remove element from the list
# li.pop()
# print(li)

# li.pop(6)
# print(li)

# # li.pop(20) #index error
# # print(li)

# li.remove(7 + 9j)
# print(li)

# # li.remove("Hello") #Value error
# # print(li)

# li.clear()
# print(li)

# #Copy()
# l1 = [1, 2, 3, 4, 5]
# l2 = l1 #Deep copy
# l3 = l1.copy() #Shallow copy
# print(l1, l2, l3)

# l1.append(6)
# print(l1, l2, l3)

#2. Array using array module
from array import array
arr = array('i', [97, 79, 7, 9])
print(arr, type(arr))

arr.append(9.7)