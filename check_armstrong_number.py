a = int(input("Enter the no. to be checked if Armstrong or not: "))
k = a
sum = 0
b = len(str(a))

while a > 0:
    remainder = a % 10
    c = remainder ** b
    sum = sum + c
    a = a // 10

if sum == k:
    print("Yes it is an Armstrong number")
else:
    print("No it is not an Armstrong number")
