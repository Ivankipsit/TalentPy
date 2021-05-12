"""
Mr.Jochen working on creating application for his school. Here are the following
functions that he would to like create -
1. get_student_marks - which takes student mark1, mark2 and mark3
and return its total.
2. get_student_grade - which calls get_student_marks and returns “A”
grade if mark1 is greater than 50, else it should return grade “B”.
3. validate_marks - which validates mark1, mark2, mark3. Here are the
validations -
1. If any of the mark is less than zero or not a number, this function
should return False.
2. If any of the mark is greater than 25, then this function should
return False.
3. Else, this function should return True
4. validate_student_name - this function should check whether student
name is of length > 5 and less than 25. If name valid, return True, else return False
5. main - Function which should take name and marks (m1, m2, m3
respectively).
a. Call validate_student_name function if it gives False, print “Invalid
Student Name”.
b. If not, Call validate_marks function and if it gives False, print
“Invalid Mark input”.
c. If not, do a simple check, ensure minimum score of each marks
(m1, m2, m3) is greater than or equal to 7. If not, print “You got failed, grades
cannot be calculated”.
d. If not, call get_student_grade method and print the grade which this
function returned as the output.
"""

def get_student_marks(m1,m2,m3):
    return m1+m2+m3

def get_student_grade(m1,m2,m3):
    if (m1+m2+m1) > 50:
        return "A"
    else:
        return "B"

def validate_marks(m1,m2,m3):
    if ((m1 or m2 or m3) < 0) or ((type(m1) or type(m2) or type(m3)) == type("123")):
        print(False)
    if ((m1 or m2 or m3) > 25):
        return False
    else:
        return True
        
def validate_student_name(name):
    if (5 < len(name) < 25):
        return True
    else:
        return False
 
def main(m1,m2,m3,name):
    if validate_student_name(name) == False:
        return "Invalid Student Name"
    if validate_marks(m1,m2,m3) == False:
        return "Invalid Mark Input"
    if (m1 >=7 and m2 >=7 and m2 >=7 ) == False:
        return "You got failed, Grades cannot be calculated"
    else:
        return get_student_grade(m1,m2,m3)


m1 = int(input("m1: "))
m2 = int(input("m2: "))
m3 = int(input("m3: "))
name = input("Name: ")

print(get_student_marks(m1,m2,m3))
print(get_student_grade(m1,m2,m3))
print(validate_marks(m1,m2,m3))
print(validate_student_name(name))
print(main(m1,m2,m3,name))