class Student:
    def __init__(self,name,student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {"English":0,"math":0,"physics":0}
    def set_grade(self,course,grade):
            if course in self.grades:
                self.grades[course] = grade
    def print_grades(self):
        print(f"{self.name} {self.student_id}:")
        for course in self.grades:
            print(f"{self.grades[course]}")

chen =Student("chen","100618")
chen.set_grade("English",92)
chen.set_grade("math",95)
chen.print_grades()
# zeng =Student("zeng","100622")
# print(chen.name)
# zeng.set_grade("math",95)
# print(zeng.grades)