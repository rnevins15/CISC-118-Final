class Person: #Creating a class
    def __init__(self, name):
        self.name = name #sets the attribute

    def customer(self):
       print(f"{self.name}")

my_person = Person("Customer")
my_person.customer()


