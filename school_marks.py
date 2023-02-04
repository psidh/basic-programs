print("Grading")

sub1 = int(input("Enter the English marks: "))
sub2 = int(input("Enter the Maths marks: "))
sub3 = int(input("Enter the Science marks: "))
sub4 = int(input("Enter the Social Science marks: "))
sub5 = int(input("Enter the Hindi marks: "))

total = sub1+sub2+sub3+sub4+sub5
avg = total/5
per = (total/500)*100

print(f"    Total Marks    -------------------------- {total}")
print(f"    Average Marks  -------------------------- {avg}")
print(f"    Percentage     -------------------------- {per}")
