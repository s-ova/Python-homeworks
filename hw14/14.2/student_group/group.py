from .student import Student

class GroupLimitError(Exception):
    """Custom exception for exceeding the number of students in a group."""
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