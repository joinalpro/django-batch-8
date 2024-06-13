student_Details = ('joinal', 'nasir', 'rayhan', 'forhad', 'tapazzal')
print('Access Item: ', student_Details[2])
print('Access Item: ', student_Details[-2])

# range
print('range', student_Details[:3])
print('range', student_Details[:-1])
print(type(student_Details))

student_list = list(student_Details)
print(type(student_list))
student_list[1] = "Nasir Patwary"
print(student_list)
updated_student = tuple(student_list)
print(type(updated_student))
print(updated_student)

# add
# cd = list(updated_student)
# cd.append('Abdulla')
# details = tuple(cd)
# print(details)

# remove
# cd = list(details)
# cd.remove('Abdulla')
# details=tuple(cd)
# print(details)