def odd_nums(n):
    for i in range(1, n+1, 2):
        yield i
a = odd_nums(30)
print(*a)
print(type(a))