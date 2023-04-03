# num1 = [1, 2, 3, 0, 0, 0]
# num2 = [4, 5, 6]
# m, n = len(num1), len(num2)
#
# # output = [1, 2, 3, 4, 5, 6] m+n = len(m+n)
#
# for i in num1:
#     if i != 0:
#         num2.append(i)
# print(len(num2))
# print(sorted(num2), num2)

# list1 = [1,2,4]
list1 = []
# list2 = [1,3,4]
list2 = [0]
Output= [1,1,2,3,4,4]

if list1:
    for val in list1:
        list2.append(val)
    print(sorted(list2))

else:
    # return []
    print(list2)
