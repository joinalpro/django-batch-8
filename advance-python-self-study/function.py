# input, process, output
# defination def

def student_result(mark):
    if mark >= 80:
        return 'A+'
    elif mark >=70 and mark <=79:
        return 'A'
    elif mark >= 60 and mark <= 69:
        return 'B'
    elif mark >= 50 and mark <= 59:
        return 'C'
    elif mark >= 40 and mark <= 49:
        return 'D'
    else:
        return 'failed'

# st_mark = student_result(int(input('insert your mark: ')))
# print("You result is : ", st_mark)
# print(student_result)
mark_list = [33, 55, 77, 88, 99]
for item in mark_list:
    print(student_result(item))