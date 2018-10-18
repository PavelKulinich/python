# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class Common:
    def __init__(self, name, surname, birth_date, school):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.school = school

    def get_full_name(self):
        return "Полное имя: {}".format(self.name + ' ' + self.surname)


class Student(Common):
    def __init__(self, name, surname, birth_date, school, class_room, father, mother):
        Common.__init__(self, name, surname, birth_date, school)
        self._class_room = {'class_num': int(class_room.split()[0]),
                            'class_char': class_room.split()[1]}
        self.father = father
        self.mother = mother

    @property
    def get_short_name(self):
        return self.surname + ' ' + self.name[0] + '.' + self.father[0] + '.'

    @property
    def parents(self):
        parents_names = str(self.father) + ' и ' + str(self.mother)
        return "Родители ученика '{}': {}".format(self.get_short_name, parents_names)

    @property
    def class_room(self):
        return "{} {}".format(self._class_room['class_num'], \
                                                   self._class_room['class_char'])

    def list_of_classes(students):
        list_of_classes = []
        for Student in students:
            if Student.class_room not in list_of_classes:
                list_of_classes.append(Student.class_room)
        print("Список всех классов школы: {}".format(list_of_classes))

    def classmates(students):
        list_of_classes = []
        for Student in students:
            if Student.class_room not in list_of_classes:
                list_of_classes.append(Student.class_room)

        for i in list_of_classes:
            classmates = []
            for Student in students:
                if i == Student.class_room:
                    classmates.append(Student.get_short_name)
                    a = Student.class_room
            print("Список учеников класса {}: {}".format(a, classmates))


class Teacher(Common):
    def __init__(self, name, surname, birth_date, school, teach_classes, discipline):
        Common.__init__(self, name, surname, birth_date, school)
        self.teach_classes = list(teach_classes)
        self.discipline = list(discipline)

    def list_of_teachers(self,teachers):
        list_of_classes2 = []
        for Teacher in teachers:
            for i in self.teach_classes:
                if i not in list_of_classes2:
                    list_of_classes2.append(i)
        for j in list_of_classes2:
            list_of_teachers = []
            for Teacher in teachers:
                if j in Teacher.teach_classes:
                    list_of_teachers.append(Teacher.get_full_name())
            print("Список учителей класса {}: {}".format(j, list_of_teachers))

def list_of_disciplines(students, teachers):
    for Student in students:
        courses = []
        for Teacher in teachers:
            if Student.class_room in Teacher.teach_classes:
                courses.append(Teacher.discipline)
        print("Список предметов уч-ка {}: {}".format(Student.get_short_name, courses))

students = [Student("Александр", "Иванов", '10.11.1998', "Лицей №5", "5 А", "Семён", "Ольга"),
            Student("Анастасия", "Соколова", '10.05.1998', "Лицей №5", "5 А", "Василий", "Наталья"),
            Student("Алексей", "Сидоров", '12.03.1998', "Лицей №5", "5 Б", "Дмитрий", "Елена"),
            Student("Василиса", "Сидорова", '07.04.1998', "Лицей №5", "5 Б", "Дмитрий", "Елена"),
            Student("Матвей", "Чижиков", '11.05.1998', "Лицей №5", "5 В", "Константин", "Валерия"),
            Student("Дмитрий", "Питонов", '16.06.1998', "Лицей №5", "5 В", "Станислав", "Екатерина"),
            Student("Алёна", "Комиссарова", '15.04.1996', "Лицей №5", "7 А", "Василий", "Марина"),
            Student("Никита", "Фича", '03.05.1996', "Лицей №5", "7 А", "Сергей", "Оксана"),
            Student("Анна", "Обновлюха", '11.02.1996', "Лицей №5", "7 Б", "Александр", "Ксения"),
            Student("Петр", "Владимиров", '17.06.1996', "Лицей №5", "7 Б", "Алексей", "Анастатия"),
            Student("Мария", "Петрова", '12.07.1996', "Лицей №5", "7 Б", "Николай", "Маргарита"),
            ]

teachers = [Teacher("Сергей", "Михайлов", '07.10.1978', "Лицей №5", ["7 А", "7 Б"], \
                    ["Информатика", "Физкультура"]),
            Teacher("Леонид", "Вассерман", '10.03.1965', "Лицей №5", ["5 А", "5 Б", "5 В", "7 А", "7 Б"], \
                    ["Алгебра", "Геометрия", "Физика"]),
            Teacher("Валентина", "Вассерман", '10.03.1971', "Лицей №5", ["7 А", "7 Б"], ["Химия", "Биология"]),
            Teacher("Екатерина", "Васильева", '10.03.1995', "Лицей №5", ["5 А", "5 Б", "5 В", "7 А", "7 Б"], \
                    ["Иностранный язык"]),
            Teacher("Анна", "Добрая", '10.03.1965', "Лицей №5", ["7 А", "7 Б"], ["История", "Обществознание"]),
            Teacher("Валентина", "Петрова", '11.09.1959', "Лицей №5", ["5 А", "5 Б", "5 В", "7 А", "7 Б"], \
                    ["Русский язык", "Литература"]),
            ]

print("РОДИТЕЛИ УЧЕНИКА")
print(students[0].parents)

print("КЛАССЫ")
print(Student.list_of_classes(students))

print("УЧИТЕЛЯ КЛАССОВ")
#print(Teacher.list_of_teachers(teachers))

print("УЧЕНИКИ КЛАССОВ")

print(Student.classmates(students))

print("ПРЕДМЕТЫ УЧЕНИКА")

# Преподаватель обязательно ведёт все свои предметы во всех своих классах
print(list_of_disciplines(students, teachers))

print("=====================СПИСОК ВСЕХ УЧЕНИКОВ ШКОЛЫ=======================")
for num, Student in enumerate(students, start=1):
   print("{}) {} {} {}".format(num, Student.get_short_name, Student.class_room, Student.parents))
