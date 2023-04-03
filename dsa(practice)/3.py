# Binary search
def binary_search(arr, size, x):
    low = 0
    high = len(arr)
    mid = size//2
    while low <= high:
        if arr[mid] == x:
            return arr[x]
        elif arr[mid] > x:
            high -= 1
        else:
            low += 1
    return arr[mid]


arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
size = len(arr)
x = 0
print(binary_search(arr, size, x))