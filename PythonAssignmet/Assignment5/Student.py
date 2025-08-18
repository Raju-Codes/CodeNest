name = input("Enter the Student's Name: ")
mark = int(input(f"{name}'s Mark: "))
student = {name: mark}
search = input("Enter the Student's Name: ")
if search in student:
    print(f"{name}'s mark is {student[search]}")
else:
    print("Student not found.")