res = 1
for i in range(1, 6):
    res = res * i
print(res)

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)
print(fact(5))