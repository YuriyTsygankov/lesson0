grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_students = sorted(students)
dict_students = dict()
students_1 = sorted_students[0]
students_2 = sorted_students[1]
students_3 = sorted_students[2]
students_4 = sorted_students[3]
students_5 = sorted_students[4]
rating_average_1 = sum(grades[0]) / len(grades[0])
rating_average_2 = sum(grades[1]) / len(grades[1])
rating_average_3 = sum(grades[2]) / len(grades[2])
rating_average_4 = sum(grades[3]) / len(grades[3])
rating_average_5 = sum(grades[4]) / len(grades[4])
dict_students = {
    students_1: rating_average_1,
    students_2: rating_average_2,
    students_3: rating_average_3,
    students_4: rating_average_4,
    students_5: rating_average_5
}
print(dict_students)
