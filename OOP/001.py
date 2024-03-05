def main():
    student = Student.get()
    print(student)

class Student:
    def __init__(self, name, house): #instance method
        self.name = name #instace variable
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

if "__main__" == __name__:
    main()
    