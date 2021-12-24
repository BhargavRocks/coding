def fibseries(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibseries(n - 1) + fibseries(n - 2)




c = int(input("Enter the no. to be checked if it is fib number or not: "))
b = 1
l = []
for i in range(c + 5):
    l.append(fibseries(b))
    b = b + 1
print(l)
if c in l:
    print("Yes it is a fib series member")
else:
    print("No it is not a fib series member")
