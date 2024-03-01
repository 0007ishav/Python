marks = int(input("What's your marks: "))

if marks > 100:
    print("Wrong Grading")
    # grade = "NULL"
    exit()


elif marks >= 90:
    grade = "A"
    

elif marks >= 80:
    grade = "B"

elif marks >= 70:
    grade = "C"

elif marks >= 60:
    grade = "D"

else:
    grade = "F"

print("Grades: ", grade)