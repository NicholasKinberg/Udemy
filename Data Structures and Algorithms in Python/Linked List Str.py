# always think of logic of solution before googling code, this is how to avoid cheating
# look at other people's code to obtain logic, not the code itself
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def str(self):
        return f"Person {self.name} - {self.age}"

new_person = Person("Nicholas", 26) 
print(new_person)