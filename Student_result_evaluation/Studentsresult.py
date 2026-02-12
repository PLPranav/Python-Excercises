name = input("Enter student name: ")
maths = float(input("Enter Maths marks: "))
science = float(input("Enter Science marks: "))
english = float(input("Enter English marks: "))

if (maths < 0 or maths > 100 or 
    science < 0 or science > 100 or 
    english < 0 or english > 100):
    print("Invalid marks entered")
else:
    total_marks = maths + science + english
    average = total_marks / 3

    
    if maths < 40 or science < 40 or english < 40:
        status = "FAIL"
    else:
        status = "PASS"

    grade = ""
    if status == "PASS":
        if average >= 75:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 40:
            grade = "C"

    print(f"\nStudent Name: {name}")
    print(f"Total Marks: {total_marks}")
    print(f"Percentage: {average:.2f}")
    print(f"Status: {status}")
    
    if status == "PASS":
        print(f"Grade: {grade}")