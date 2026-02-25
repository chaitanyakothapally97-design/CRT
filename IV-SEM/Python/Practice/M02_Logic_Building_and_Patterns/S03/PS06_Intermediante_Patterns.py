# li = [1, 2, 3, 4, 5]
# res = []
# print([ele * 2 for ele in li])
# # print(res)

# li = [1, 2, 3, 4, 5]
# res = []
# # for ele in li:
# #     if(ele % 2 == 0):
# #         res.append(ele)
# # print(res)
# print([ele for ele in li if ele % 2 == 0])
# print(tuple(ele for ele in li if ele % 2 == 0))
# print({ele:ele * 2 for ele in li if ele % 2 == 0})

# li = ['a', 'b', 'c']
# # print(* li)
# print(" ".join(li))

# Pyramid pattern:
# n = int(input("Enter a number: "))
# # for i in range(n, 0, -1):
# #     # for _ in range(n - i):
# #     #     print(" ", end = "")
# #     # for j in range(i):
# #     #     print("*" , end = " ")
# #     # print()
# #     print(" " * (n - i) + "* " * i)

# for i in range(n + 1):
#     print(" " * (n - i) + "* " * i)
# for i in range(n - 1, 0, -1):
#     print(" " * (n - i) + "* " * i)

n = int(input("Enter a number: "))
" ".join([str(i)for i in range(n, 0, -1)])
print(i, end = "") # type: ignore
" ".join([str(i)for i in range(2, n + 1, +1)])
print(i, end = "") # type: ignore
