number = [ 3, 4, 6, 7]
my_iter = (iter(number))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

for item in my_iter:
    print(item)