arr = []
brr = []
for i in range(5):
    arr.append(i)
    brr.append(int(input("Enter a number: ")))

print(arr)
print(brr)
######################################
arr = [1, 2, 3, 4, [99, 100, 101], 0]
print(arr[4][2])
arr2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(arr2)

#################################
'''
arr = [[1,2,3], [4,5,6], [7,8,9]]
arr[1] = [4,5,6]
arr[1][1]]= 5
'''
multiDimension = [0, []]
for i in range(6):
    multiDimension[1].insert(1, i)
print(multiDimension)

#######################################
