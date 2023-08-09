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


st_1 = Student("sasha", 'belui', 35, "Python")
st_2 = Student('ivan', 'ivabov', 23, 'java')
st_3 =Student('oleh', 'olegov',15, 'css')
st_4 = Student('kolya', 'sidorov', 32, 'Python')


class Gruppa:

    def __init__(self, name: str):
        self.__gruppa = []
        self.name = name

    def add_student(self, student: Student):
        self.__gruppa.append(student)

    def del_student(self, student: Student):
        self.__gruppa.remove(student)

    def get_student_surname(self, surname: str):
        res = []
        x = self.surname.lower()
        for i in self.__gruppa:
            if x in i.surname.lower():
                res.append(i)
        return res



    def __str__(self):
        res = ""
        for i in self.__gruppa:
            res = res + str(i)+ '\n'
        return res

gruppa_1 = Gruppa('pervaya')
gruppa_1.add_student(st_3)
gruppa_1.add_student(st_4)
gruppa_1.add_student(st_2)
gruppa_1.add_student(st_1)

print(gruppa_1)

gruppa_1.del_student(st_3)
print(gruppa_1)
gruppa_1.get_student_surname('sidorov')