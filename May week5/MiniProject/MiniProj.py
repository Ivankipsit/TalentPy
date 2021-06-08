class Doctor:
    def __init__(self, doctor_name, specialisations, available_days, appoinment_seat, class_hospital):
        self.doctor_name = doctor_name
        self.specialisations = specialisations
        self.available_days = available_days
        self.appoinment_seat = appoinment_seat
        self.hospital_name = class_hospital.hospital_name
        self.address_of_the_hospital = class_hospital.address_of_the_hospital 
    def is_available(self, day):
        list_days = list(self.appoinment_seat.keys())
        list_no_of_appoinments = list(self.appoinment_seat.values())
        for ele in self.available_days:
            if day in list_days:
                a = list_days.index(day)
                b = list_no_of_appoinments[a]
                if b == 0:
                    return False
                else:
                    for i in range(len(list_no_of_appoinments)):
                        if list_no_of_appoinments[i] == b:
                            c = b-1
                            list_no_of_appoinments[i], c = c, list_no_of_appoinments[i]
                            self.appoinment_seat = dict(zip(self.appoinment_seat.keys(), list_no_of_appoinments))
                            return True
            else:
                return False
    def is_specialist(self, disease):
        list_specialisation = [ele.lower() for ele in self.specialisations ]
        if disease.lower() in list_specialisation:
            return True 
        else: 
            return False    
    def book_appoinment(self, day, disease):
        if Doctor.is_specialist(self, disease) == False:
            return -1 
        if Doctor.is_available(self, day) == True:
            return 1        
        if Doctor.is_available(self, day) == False:
            return 0
    def do_booking(self, day, disease):
        if Doctor.book_appoinment(self, day, disease) == 1:
            result = """
Appoinment Successful
{}\n{}\n{}\n{}\n{}\n{}
            """.format(self.doctor_name, self.hospital_name, self.address_of_the_hospital, self.name_of_patient, day, self.disease_he_has)
            return result
        if Doctor.book_appoinment(self, day, disease) == -1:
            return "\nRequested Doctor is not a specialist for your request"
        if Doctor.book_appoinment(self, day, disease) == 0:
            return "\nDoctor not available on your requested date"
class Hospital:
    def __init__(self, hospital_name, address_of_the_hospital):
        self.hospital_name = hospital_name
        self.address_of_the_hospital = address_of_the_hospital
class Patient:
    def __init__(self, name_of_patient, disease_he_has, class_doctor, class_hospital):
        self.name_of_patient = name_of_patient
        self.disease_he_has = disease_he_has
        self.hospital_name = class_hospital.hospital_name
        self.address_of_the_hospital = class_hospital.address_of_the_hospital
        self.doctor_name = class_doctor.doctor_name
        self.assigned_doctor = class_doctor.doctor_name
        self.specialisations = class_doctor.specialisations
        self.available_days = class_doctor.available_days
        self.appoinment_seat = class_doctor.appoinment_seat
    def book(self,day):
        print(Doctor.do_booking(self, day, self.disease_he_has))
#testcase passed
hospital1 = Hospital("ABC Multi-speciality Hospital", "71, South Street, Ambattur, Chennai")
doctor1 = Doctor("Dr. John", ["Diabetics", "ENT"], ["Monday", "Friday"], {"Monday" : 5, "Friday" : 1}, hospital1)
patient1 = Patient("talentpY", "Diabetics", doctor1, hospital1)
patient1.book("Friday")
patient1.book("Friday")
patient1.book("Tuesday")
patient2 = Patient("Roy", "Dengue", doctor1, hospital1)
patient2.book("Monday")
