class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def set_first_name(self, first_name):
        self.first_name = first_name
        return True
    
    def return_last_name(self):
        return self.last_name


p1 = Person("Masoud", "Kaviani")
p2 = Person("Ali", "Karimi")
ln = p1.return_last_name()
ln2 = p2.return_last_name()
print(ln)
print(ln2)