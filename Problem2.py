"""
Mr. Ashok like to create a flight ticket booking application. To book a
flight, user should enter his / her name, DOB, address and passport
number followed by Start city, destination city and date of travel. Here are
the constraints -
1. Name should be all in upper case and it should be free from special
characters or numbers. His application only allow names of length
ranges from 5 to 30 max.
2. DOB should be in a format of DD-MM-YYYY. Other formats not
allowed.
3. Passport number is only of 8 digits and should start with ‘P’
followed by numbers.
4. Start city and destination city should NOT be same. Here are the
constraints -
1. Start city / End city should be any one of these [ “Paris”,
“Japan”, “China”]
5. Date of travel should be in format [DD-MM-YYYY]
 Write functions to validate all those above constraints and if all validations
successful, return “Flight Ticket Booked”, else return respective error
message. (Example: Invalid Passport number if passport number validation
fails etc….)
"""
import datetime as dt

def check_name(name,list1):
    if (name.isupper()):
        if (len(name) < 31):
            list1.append("name")
            return "Name Verified!!!"
    else:
        return "Please enter your name in CAPS"
def check_DOB(dob,list1):
    k = []
    b = dob.split("-")
    for _ in b:
        ele = int(_)
        k.append(ele)
    dob1 = dt.date(k[2], k[1], k[0])
    dob1 = f"{dob1:%d-%m-%Y}"
    if(dob == dob1):
        list1.append("dob")
        return "Date of Birth Verified!!!"
    else:
        return "Please enter dob in DD-MM-YYYY format"
def check_Pass(passport,list1):
    a = passport[1:]
    a = int(a)
    if (len(passport) == 8):
        if passport[0] == "P":
            if (0000000 < a < 9999999):
                list1.append("Pass")
                return "Passport Verified"
            else:
                return "Please enter valid passport number."    
        else:
            return "Please enter valid passport number."
    else:
        return "Please enter valid passport number."
def check_startanddest(startcity, destcity,list1):
    city = [ "Paris", "Japan", "China"]
    if startcity in city:
        if destcity in city:
            if startcity == destcity:
                return "Please check starting city and destination." 
            else:
                list1.append("Dest")
                return "Destination Verified!!! "
    else:
        return "Please pick starting city and destination from - Paris, Japan, China."
def check_DOTravel(dot,list1):
    k = []
    b = dot.split("-")
    for _ in b:
        ele = int(_)
        k.append(ele)
    dot1 = dt.date(k[2], k[1], k[0])
    dot1 = f"{dot1:%d-%m-%Y}"
    if(dot == dot1):
        list1.append("dot")
        return "Date of Travel Verified!!!"
    else:
        return "Please enter date of travel in DD-MM-YYYY format"


list1 = []
name = input("Enter Name: ")
print(check_name(name,list1))

dob = input("Enter DOB: ")
print(check_DOB(dob,list1))

passport = input("Enter Passport number: ")
print(check_Pass(passport,list1))

startcity = input("Enter starting city: ")
destcity = input("Enter destination: ")
print(check_startanddest(startcity, destcity,list1))

dot = input("Enter date of travel: ")
print(check_DOTravel(dot,list1))

if (len(list1) == 5):
    print("Flight Ticket booked successfully")
else:
    print("Please enter all the required details correctly")


