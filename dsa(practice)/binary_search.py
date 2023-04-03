def binary(n):
    l = []
    while (n > 0):
        r = n % 2
        l.append(r)
        n = n // 2
    i = len(l)
    while (i > 0):
        print(l.pop(), end="")
        i += -1


# n = int(input('enter: the number to know the binary'))
n = [12,21,4,53,2]
binary(n)
