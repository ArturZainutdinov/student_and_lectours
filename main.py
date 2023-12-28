class Student:
    def __init__(self, name, surname, gender, ):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):  #Оценка лекторов
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            if course in lecturer.add_grades:
                lecturer.add_grades[course] += [grade]
            else:
                lecturer.add_grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self): # вывод
        in_progress_courses = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        average_grade = sum(sum(grades) for grades in self.grades.values()) / sum(len(grades) for grades in self.grades.values())

        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за доашние задания: {average_grade} \nКурсы в процессе изучения: {in_progress_courses} \nЗавершенные курсы: {finished_courses}'

    def __lt__(self, other):   # сравнение
        average_grade_self = sum(sum(grades) for grades in self.grades.values()) / sum(len(grades) for grades in self.grades.values())
        average_grade_other = sum(sum(grades) for grades in other.grades.values()) / sum(len(grades) for grades in other.grades.values())
        return average_grade_self < average_grade_other

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):
     def __init__(self, name, surname):
         super().__init__(name, surname)
         self.add_grades = {}


     def __str__(self):   # Вывод
        average_grade = sum(sum(grades) for grades in self.add_grades.values()) / sum(len(grades) for grades in self.add_grades.values())
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка: {average_grade}'


def __lt__(self, other):  # сравнение
    average_grade_self = sum(sum(grades) for grades in self.add_grades.values()) / sum(
        len(grades) for grades in self.add_grades.values())
    average_grade_other = sum(sum(grades) for grades in other.add_grades.values()) / sum(
        len(grades) for grades in other.add_grades.values())
    return average_grade_self < average_grade_other


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):   # проверка для студентов
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'






def calculate_average_grade_for_course(students, course):
    total_grades = 0
    count = 0
    for student in students:
        if course in student.courses_in_progress:
            total_grades += sum(student.grades.get(course, []))
            count += len(student.grades.get(course, []))
    if count > 0:
        average_grade = total_grades / count
    else:
        average_grade = 0
    print(f"Средняя оценка за домашние задания по курсу '{course}': {average_grade}")

def calculate_average_grade_for_lecturers(lecturers, course):
    total_grades = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.courses_attached:
            total_grades += sum(lecturer.add_grades.get(course, []))
            count += len(lecturer.add_grades.get(course, []))
    if count > 0:
        average_grade = total_grades / count
    else:
        average_grade = 0
    print(f"Средняя оценка за лекции по курсу '{course}': {average_grade}")


stu1 = Student('Андрей', 'Юлдашев', 'Female')
stu2 = Student('Фархат', 'Борисов', 'Male')
rev2 = Reviewer('Анна', 'Мамина')
rev1 = Reviewer('Михаил', 'Гросс')
lect2 = Lecturer('Юлия', 'Мухина')
lect1 = Lecturer('Юрий', 'Чернов')
stu1.courses_in_progress = ['Python', 'Java']
stu1.finished_courses = ['C', 'C++']
stu1.rate_lecture(lect1, 'Python', 9)
stu1.rate_lecture(lect2, 'Python', 8)
stu2.courses_in_progress = ['Python', 'Physics']
stu2.finished_courses = ['Math', 'English']
stu2.rate_lecture(lect1, 'Python', 7)
stu2.rate_lecture(lect2, 'Python', 6)
lect1.courses_attached = ['Python', 'java']
lect1.add_grades = {'Python': [9, 7], 'Math': [8, 6]}
lect2.courses_attached = ['Python', 'C']
lect2.add_grades = {'Python': [8, 6], 'Physics': [7, 5]}
rev1.courses_attached = ['Python', 'GO']
rev1.rate_hw(stu1, 'Python', 10)
rev1.rate_hw(stu1, 'Math', 9)
rev1.rate_hw(stu2, 'Python', 8)
rev1.rate_hw(stu2, 'Math', 7)

rev2.courses_attached = ['Python', 'DevOps']
rev2.rate_hw(stu1, 'Python', 7)
rev2.rate_hw(stu1, 'Physics', 6)
rev2.rate_hw(stu2, 'Python', 9)
rev2.rate_hw(stu2, 'Physics', 8)



students = [stu1, stu2]
course = "Python"  # название курса
calculate_average_grade_for_course(students, course)

lecturers = [lect1, lect2]
calculate_average_grade_for_lecturers(lecturers, course)


print(stu1 < stu2)