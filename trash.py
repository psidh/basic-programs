STUDENTS = []

student_A = []
student_B = []
student_C = []
strength_of_class = int(input("Enter the strength of the class: "))

for i in range(strength_of_class):
    fname  =  input("Enter your first name: ")
    mname  =  input("Enter your middle name: ")
    lname  =  input("Enter your last name: ")

    marks  =  int(input("Enter your marks: "))

    name  = fname+ " " + mname + " " + lname

    sub_list = [name, marks]
    STUDENTS.append(sub_list)   

for i in range(strength_of_class):
    if STUDENTS[i][1] > 80:
        student_A.append(name)
    elif 60 <= STUDENTS[i][1] <= 80:
        student_B.append(name)
    elif STUDENTS[i][1] < 60:
        student_C.append(name)

print(f"The list of all the students are \n {STUDENTS}")
print(f"The list of A grade students \n {student_A}")
print(f"The list of B grade students \n {student_B}")
print(f"The list of C grade students \n {student_C}")


# #print all students list, A and B and C grade list separately



