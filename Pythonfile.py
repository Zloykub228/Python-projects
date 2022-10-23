'''
def summary():
    x = int(input('x= '))
    y = int(input('y= '))

    return print(f'Добуток степеню x та y = {x**y}')

summary()
'''
class Student():
    print('Darova eto kurs python')
    amount_of_students = 0
    def __init__(self, height = 170):
        self.height=height
        Student.amount_of_students +=1


first_student = Student()
second_student = Student()
student_3=Student(height=175)
#Student.__init__(self=first_student)
print('first_student-', first_student.height)
print('second_student-', second_student.height)
print('student_3-', student_3.height)
print('first_student-', first_student.amount_of_students)
print('second_student-', second_student.amount_of_students)
print('student_3-', student_3.amount_of_students)