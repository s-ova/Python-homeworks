class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old, {self.gender}"

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__}, Record Book: {self.record_book}"

class GroupLimitError(Exception):
    """Custom exception for exceeding the number of students in a group"""
    def __init__(self, message="Group limit exceeded. Maximum 10 students allowed."):
        super().__init__(message)

class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()
        self.max_students = 10

    def add_student(self, student):
        if len(self.group) >= self.max_students:
            raise GroupLimitError()
        if isinstance(student, Student):
            self.group.add(student)
        else:
            raise ValueError("Only objects of type Student can be added to the group")

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = "\n".join(str(student) for student in self.group)
        return f"Group Number: {self.number}\nStudents:\n{all_students}"

students = [
    Student('Male', 20, f'Student{i}', f'Lastname{i}', f'RB{i:03}') for i in range(11)
]

gr = Group('PD1')

for i, student in enumerate(students):
    try:
        gr.add_student(student)
        print(f"Added: {student}")
    except GroupLimitError as e:
        print(f"Cannot add {student.first_name} {student.last_name}: {e}")

print(gr)

"""
Group Number: PD1
Students:
(Student information for up to 10 students)
"""

assert str(gr.find_student('Lastname0')) == str(students[0]), 'Test1'
assert gr.find_student('Lastname10') is None, 'Test2'
assert isinstance(gr.find_student('Lastname1'), Student) is True, 'The search method must return an instance'

gr.delete_student('Lastname1')
print(gr)
"""
Group Number: PD1
Students:
(Updated list of students)
"""


