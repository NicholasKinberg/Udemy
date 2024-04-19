class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def str(self):
        return f"Person {self.name} - {self.age}"

new_person = Person("Nicholas", 26) 
print(new_person)