# default argument
# positional argument
# keyword argument

# def multiply (x, y, z):
#     return x + y

# print(multiply(2, 2))

# def student_marks(a, b=4):
#     return a + b

# print(student_marks(4))

# star(*) argument / *args
def divide_by (*args):
    for num in args:
        print(f"{num * 2} showing multple result")
divide_by(2, 3, 4, 6)