"""
Create a class Printer with a default constructor and a method called print_me(data), which
returns the data that comes as argument.
"""

class Printer:
    def __init__(self):
        self.data = ""
        
    def print_me(self,data):
        return data
        
data1 = Printer()
print(data1.print_me("good")) #good
