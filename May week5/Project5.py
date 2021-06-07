class formal_name:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def formal_attire(self):
        a = self.gender
        if a.lower() == "male":
            return " Mr.{}".format(self.name)
        if a.lower() =="female":
            return " Ms.{}".format(self.name)
obj1 = formal_name("Mike","Male")
obj2 = formal_name("Jance","Female")
print(obj1.formal_attire())
print(obj2.formal_attire())
