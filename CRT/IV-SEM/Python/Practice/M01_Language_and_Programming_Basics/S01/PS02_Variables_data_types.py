'''
Data types:
1. Fundamental DT:
    1. int
    2. float
    3. complex
    4. Boolean
    5. String

2. Collection DT:
    1. List
    2. Tuple
    3. Set
    4. Dictionary
'''
x = 97
y = 97.97
z = 9 + 7j
print(type(x))
print(type(y))
print(type(z))

f1 = 7e9
f2 = 9E7
print(f1, type(f1))
print(f2, type(f2))

c1 = 9 + 7j
c2 = complex(7, -9)
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)
print(c1.real, c1.imag)
print(c2.real, c2.imag)

s = "Chaitu"
print(s[2])
print(s[::])
print(s[::-1])
print(s[::2])