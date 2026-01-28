'''n = int(input())
temp = n
count = 0
while n > 0:
    n //= 10
    count += 1
print(count)
print(len(str(temp)))'''
# #2 Find the sum of digits of a number
# n = int(input())
# s = 0
# while n > 0:
#     s += (n % 10)
#     n //= 10
# print(s)

# n = int(input())
# e_count = 0
# o_count = 0
# while n > 0:   
#     n //= 10
#     if (n // 10) % 2 == 0:
#         e_count += 1
#     else:
#         o_count += 1
# print(e_count)
# print(o_count)

n = int(input())
while n > 0:
    n = sum(list(map(int, str(n))))
print(n)