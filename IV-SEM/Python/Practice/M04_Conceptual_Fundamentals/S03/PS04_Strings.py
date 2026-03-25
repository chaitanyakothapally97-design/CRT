#string is a collection of characters enclosed in qoeutes
#string is immutable

# s = "python"
# s1 = "python"
# s2 = '''
# python
# is
# interesting'''
# print(s + s2) #concatenation
# print(s1 * 2) #repetition
# print("on" in s)

'''s = "python"
print(len(s))
print(max(s))
print(max("abc123ABC"))
print(min("abc123ABC"))'''
'''
#Built-in Methods
s = "python"
s = s.replace("y", "Y")
print(s)

#print(dir(str))

print(s.find("on"))
print(s.find("yes"))'''

#Reverse a string using slicing
s = "python"
print(s[::-1])

#Reverse a string without using slice range operator
s = "python"
rev = ""
for i in s:
    rev = i + rev
print(rev)
#check whether string is pallindrome or not
if rev == s:
    print("Pallindrome")
else:
    print("Not a pallindrome")

#check wether string is Anagram or not
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not an Anagram")

#use counter to check frequency of values
from collections import Counter
print(Counter(s1))

#check wether string is Anagram or not without using builtin functions
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
def anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    count = {}
    for i in s1:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    for i in s2:
        if i in count:
            count[i] -= 1
        else:
            count[i] = 1
    for i in count:
        if count[i] != 0:
            return False
    return True