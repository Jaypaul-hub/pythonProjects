score=float(input("Enter marks of student: "))
if score<0 or score>100:
    print("Enter marks in range 0 to 100")
elif score>=80:
    print("Grade A")
elif score>=70:
    print("Grade B")
elif score>=60:
    print("Grade C")
elif score>=50:
    print("Grade D")
else:
    print("grade F")