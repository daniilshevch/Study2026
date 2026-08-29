class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_person(self):
        print(f"Name: {self.name}, Age: {self.age}")

if __name__ == "__main__":
    person1 = Person("Alice", 30)
    person1.print_person()
    person2 = Person("Bob", 25)
    person2.print_person()