students = ["Raj", "Priya", "Amit", "Sneha", "Karan"]
subjects = ("Math", "Science", "English")
marks_data = {
    "Raj": [85, 78, 90],
    "Priya": [92, 88, 85],
    "Amit": [70, 75, 68],
    "Sneha": [95, 90, 92],
    "Karan": [80, 82, 78]
}
unique_grades = set()
top_score = -1
top_student = ""
print(f"All Students: {students}")
print(f"First 3 Students: {students[:3]}\n")
for student in students:
    marks = marks_data[student]
    avg = sum(marks) / len(marks)
    
    if avg >= 85:
        grade = "A"
    elif avg >= 70:
        grade = "B"
    else:
        grade = "C"
    
    unique_grades.add(grade)
    
    print(f"{student} - Average: {avg:.2f} - Grade: {grade}")
    
    if avg > top_score:
        top_score = avg
        top_student = student

print(f"\nTop Student: {top_student}")

print(f"Unique Grades: {set(sorted(unique_grades))}")
