# # # a = int(input())
# # # if (a % 4 == 0) and (a % 100 != 0) or (a % 400 == 0):
# # #     print('yes')
# # # else:
# # #     print('no')
# # for i in range(1, 101, 2):
# #     if i % 13 == 0:
# #         print(i)
# a = [1, 31, -3, 111, -8, 0, 7]
# q = a[0]
# for i in range(len(a)):
#     if q > a[i]:
#         q = a[i]
# print(q)
# a = list(map(int, input().split()))
# # q = a[0]
# # for i in range(len(a)):
# #     if i %2 ==1:
# #         if q > a[i]:
# #             q = a[i]
# print(a)
# print(input().split())
# map(print, [3, 14, -8, 0])
# task 1, https://informatics.msk.ru/mod/statements/view.php?id=4163&chapterid=3838#1
# a = list(input())
# b = list()
# for i in range(len(a)):
#     if a[i] not in b:
#         b.append(a[i])
# print(len(b))
# task 2, https://informatics.msk.ru/mod/statements/view.php?id=4163&chapterid=3839#1
# a = list(map(int, input().split()))
# print(a[::-1])
# task 3, https://informatics.msk.ru/mod/statements/view.php?id=4163&chapterid=3843#1
# a = list(map(int, input().split()))
# mi = a[0]
# ma = mi
# kma = 0
# kmi = 0
# z = 0
# for i in range(len(a)):
#     if mi > a[i]:
#         mi = a[i]
#         kmi = i
#     if ma < a[i]:
#         ma = a[i]
#         kma = i
# z = mi
# a[kmi] = a[kma]
# a[kma] = z
# print(a)
a = list(map(int, input().split()))
print(a)
