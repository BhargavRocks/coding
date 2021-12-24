
n = int(input("Enter the number of rows of ABCD patter to be printed: "))
i = n
while i >= 1:
    start = chr(ord('A') + n - 1 + i - 1)
    j = n
    while j >= i:
        p = chr(ord(start) - j + 1)
        print(p, end=" ")
        j = j - 1
    i = i - 1
    print()