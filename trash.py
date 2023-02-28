LIST_OF_ALL_STUDENTS = []
student_A = []
student_B = []
student_C = []
strength_of_class = int(input("Enter the strength of the class: "))

for i in range(strength_of_class):
    fname  =  input("Enter your first name: ")
    mname  =  input("Enter your first name: ")
    lname  =  input("Enter your first name: ")

    marks  =  input("Enter your first name: ")

    name  = fname+ " " + mname + " " + lname

    LIST_OF_ALL_STUDENTS.append(name)
    
    if marks > 80:
        student_A.append(name)
    elif 70 < marks <= 80:
        student_B.append(name)
    else:
        student_C.append(name)

print(f"The list of all the students are \n {LIST_OF_ALL_STUDENTS} \n ")
print(f"The list of A grade students \n {student_A}")
print(f"The list of B grade students \n {student_B}")
print(f"The list of C grade students \n {student_C}")
