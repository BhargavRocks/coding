# //pgm for diamond pattern

n = int(input())  # //input from the user is stored in n
x = n // 2 + 1
# //here two loops are combined into one by 'zip'
# //loop for printing the first half diamond
for i, j in zip(range(1, x + 1), range(1, n + 1, 2)):
    print(' ' * (x - i) + '*' * (j))
# //loop for printing the second half diamond(reverse half)
for i, j in zip(range(1, x + 1), range(n - 2, -1, -2)):
    print(' ' * (i) + '*' * (j))
