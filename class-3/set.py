# python set
# number = {3, 4, 2, 2, 5, 2, 5, 2, 6}
# print(type(number))
# print(number)

# access items
# for x in number:
#     print('Access item: ', x)

# add method
# number = {3, 4, 2, 2, 5, 2, 5, 2, 6}
# number.add(8)
# print(number)

# set, union, intersection
# a = {3, 4, 5, 23,25,6, 7, 4}
# b = {89,4,2,4,25}
# print('Union Method ', a | b)
# print('Union Method ', a & b)
    
shopSerial = {2, 4, 1, 5, 3, 6, 3, 2, 7, 5, 6, 4}
ownerSerial = {4, 6, 8, 3, 2, 5, 3, 4, 6, 7}
# print(shopSerial)
# for i in shopSerial:
#     print("Only unique number will show: ", i)
# shopSerial.add(8)
# print(shopSerial)

# print("Union Method: ", shopSerial | ownerSerial)
# print("Union Method: ", shopSerial & ownerSerial)
for x in shopSerial:
    print("Access Item ",x)

print(9 in shopSerial)