import operation
from students import Student
from teachers import Teachers
print(operation.add_numbers(11,23))
print(operation.sub_numbers(12,6))
print(operation.div_numbers(110,11))
print(operation.mult_numbers(32,78))


new_student = Student('john','swimming',2003)
new_student.greetStudent()

new_teacher = Teachers('john',12563,'mathematics',100000)
print(new_teacher.get_tcs_no())