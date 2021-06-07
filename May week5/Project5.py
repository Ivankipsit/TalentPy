class formal_name:
	def __init__(self, name, gender):
		self.name = name
		self.gender = gender
	def formal_attire(self):
		self.gender.lower()
		if self.gender == "male":
			return " Mr.{}".format(self.name)
		if self.gender =="female":
			return " Ms.{}".format(self.name)
	
obj1 = formal_name("Mike","Male")
print(obj1.formal_attire()) 
