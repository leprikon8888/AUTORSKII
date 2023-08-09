class Human:

    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f'Name = {self.name}\n Surname = {self.surname}\n Age = {self.age}'


class Student(Human):

    def __init__(self, name: str, surname: str, age: int, course: str ):
        super().__init__(name, surname, age)
        self.course = course

    def __str__(self):
        return f"Student:  {self.surname} {self.name} studies {self.course}"





class Gruppa:

    def __init__(self, name: str):
        self.__gruppa = []
        self.name = name

    def add_student(self, student: Student):
        self.__gruppa.append(student)

    def del_student(self, student: Student):
        self.__gruppa.remove(student)

    def get_student_surname(self, sur: str):
        res = []
        result = ''
        for student in self.__gruppa:
            if sur.lower() in student.surname.lower():
                res.append(student)

        for item in res:
            result+= str(item) + '\n'
        return result



    def __str__(self):
        res = ""
        for i in self.__gruppa:
            res = res + str(i)+ '\n'
        return res

st_1 = Student("Саша", 'Белый', 35, "Python")
st_2 = Student('Иван', 'Иванов', 23, 'Java')
st_3 = Student('Олег', 'Олегов', 15, 'CSS')
st_4 = Student('Коля', 'Сидоров', 32, 'Python')
st_5 = Student('oles', 'сИдоров', 33, 'java')
st_6 = Student('kiril', 'Сидоров', 27, 'python')


gruppa_1 = Gruppa ('Первая')
gruppa_1.add_student(st_3)
gruppa_1.add_student(st_4)
gruppa_1.add_student(st_2)
gruppa_1.add_student(st_1)
gruppa_1.add_student(st_5)
gruppa_1.add_student(st_6)





print(gruppa_1.get_student_surname('сидор'))