grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
average_grades = []
for marks in grades:
    average = sum(marks) / len(marks)
    average_grades.append(round(average, 2))
# average_grades = [round(sum(marks) / len(marks), 2) for marks in grades] помог преподаватель
students_list = sorted(students)
book = {}
for num in range(len(students_list)):
    book[students_list[num]] = average_grades[num]
# for num, student in enumerate(students_list):
#     book[student] = average_grades[num] помог преподаватель
print(book)





