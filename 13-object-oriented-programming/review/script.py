class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []
        self.attendance = {}

    def __repr__(self):
        return "Student: {} Year:{}\nGrades:{}\nAverage Score:{:2f}\n".format(self.name, self.year, self.get_grades(), self.get_average())

    def add_grade(self, grade):
        if (isinstance(grade, Grade)):
            self.grades.append(grade)

    def get_grades(self):
        sum = 0
        for grade in self.grades:
            sum += grade.score
        return sum

    def add_attendance(self, date, status):
        self.attendance[date] = status

    def get_attendance(self,date):
        return self.attendance.get(date,False)

    def get_average(self):
        sum = 0
        for grade in self.grades:
            sum += grade.score
        return sum / len(self.grades)


class Grade:
    minimum_passing = 65

    def __init__(self, score):
        self.score = score

    def __repr__(self):
        return "abc"

    def is_passing(self):
        return self.score >= self.minimum_passing


roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

roger.add_grade(Grade(68))
roger.add_grade(Grade(79))
roger.add_grade(Grade(88))
roger.add_attendance("01/22/2020", True)
roger.add_attendance("01/25/2020", False)
roger.add_attendance("01/20/2020", True)

sandro.add_grade(Grade(73))
sandro.add_grade(Grade(98))
sandro.add_grade(Grade(85))
sandro.add_attendance("01/22/2020", True)
sandro.add_attendance("01/25/2020", False)
sandro.add_attendance("01/20/2020", True)

pieter.add_grade(Grade(99))
pieter.add_grade(Grade(77))
pieter.add_grade(Grade(79))
pieter.add_attendance("01/22/2020", True)
pieter.add_attendance("01/25/2020", False)
pieter.add_attendance("01/20/2020", True)

print(roger)
print(sandro)
print(pieter)
print("=====================")
print(f"Was {roger.name} in attendance on '24 Jan 2020?' : {roger.get_attendance('01/22/2020')}")
