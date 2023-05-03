# find = open("week06_functions.py", "r")
# output = open("functions.txt", "w")
# for line in find:
#     if line.startswith("def "):
#         output.write(line)
# find.close()
# output.close()
#
# def find_functions(filename: str) -> None:
#     with open(filename, 'r') as find:
#         with open("functions.txt", "w") as out_put:
#             for line in find:
#                 if line.startswith('def '):
#                     out_put.write(line)
#
#
# find_functions("week06_functions.py")
#
# def find_functions(filename: str) -> list[tuple]:
#     function = []
#     with open(filename, 'r') as find:
#         for count, line in enumerate(find, 1):
#             if line.startswith('def '):
#                 line = line.split('def ')[1]
#                 name, _, line = line.partition('(')
#                 args, _, _ = line.partition(')')
#                 args = tuple(args.split(', '))
#                 function.append((count, name, args))
#     return function
#
#
# find_functions("week06_functions.py")
#
#
# def read_config(filename) -> dict:
#     config = {}
#     heading = None
#     with open(filename, 'r') as find:
#         for line in find:
#             line = line.strip()
#             if line.startswith('[') and line.endswith(']'):
#                 heading = line[1:-1]
#                 config[heading] = {}
#             elif line.count("=") == 1 and heading is not None:
#                 name, value = line.split("=")
#                 config[heading][name] = value
#
#     return config
#
#
# print(read_config("week06_config.txt"))
#
#
# def get_value(config, value) -> str:
#     heading, name = value.split(".")
#
#     return config[heading][name]
#
#
# print(get_value(read_config("week06_config.txt"), 'user.mobile'))


class Student(object):
    def __init__(self, name, student_num, degree):
        self._name = name
        self._student_num = student_num
        self._degree = degree
        self._grades = {}

    def get_name(self):
        return self._name

    def get_student_num(self):
        return self._student_num

    def get_degree(self):
        return self._degree

    def set_degree(self, degree):
        self._degree = degree

    def get_first_name(self):
        return self._name.split()[0]

    def get_last_name(self):
        return self._name.split()[1]

    def get_email(self):
        return "{}.{} @uq.net.au".format(self.get_last_name().lower(),
                                         self.get_first_name().lower())

    def __str__(self):
        return "{} ({}, {}, {})".format(self.get_name(), self.get_email(),
                                        self._student_num, self._degree)

    def __repr__(self):
        return "Student({0!r}, {1}, \'{2}\')".format(s._name,
                                                     s._student_num, s._degree)

    def add_gpa(self, course, grade):
        self._grades[course] = grade

    def gpa(self):
        if self._grades == {}:
            return 0.0
        else:
            return sum(self._grades.values())


def check_students(students: list[Student]):
    number = []
    for student in students:
        student_num = student.get_student_num()
        if student_num in number:
            return False
        number.append(student_num)
    return True


class Course(Student):
    def __init__(self, course, grade, name, student_num, degree):
        super().__init__(name, student_num, degree)
        self._course = course
        self._grade = grade

    def add_grade(self, course, grade):
        self._course = course
        self._grade = grade

    def gpa(self):
        return self._grade


s = Student('Jesse Jack', '0949585930', 'Bachelor')
print(s.get_name())
print(s.get_student_num())
print(s.get_degree())
s.set_degree('BF')
print(s.get_degree())
print(s.get_first_name())
print(s.get_last_name())
print(s.get_email())
print(s.__str__())
print(s.__repr__())
students1 = [Student('Alice A', 1, 'BE'),
             Student('Bob B', 2, 'BA'),
             Student('Carol C', 4, 'BA')]
students2 = [Student('Alice A', 1, 'BE'),
             Student('Bob B', 2, 'BA'),
             Student('Carol C', 4, 'BA'),
             Student('Dan D', 2, 'BInfTech')]
print(check_students(students2))
