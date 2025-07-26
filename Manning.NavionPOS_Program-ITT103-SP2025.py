import datetime
import random

#Name: Navion Manning
#Student ID number : 20246095
#Course: Programming Technique
#Lecturer: Jonathan Johnson
#Semester: Summer 2025



class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


class Patient(Person):
    def __init__(self, name, age, gender):
        super().__init__(self, name, age, gender)
        self.patient_id = patient_id_no()
        self.appointment_list = []

def __str__(self):
    return f"Patient ID: {patient_id_no()},Name: {self.name},Age:{self.age}, Gender {self.gender}"

#Generate patients id
def patient_id_no():
    return random.randint(10000, 150000)


class Doctor(Person):
    def __init__(self, speciality, name, age, gender):
        super().__init__(self, name, age, gender)
        self.doctor_id = doctor_id_no()
        self.speciality = speciality
        self.schedule = []
#Generate doctors id number using random method
def doctor_id_no():
    return random.randint(156789, 1987650)


class Appointments:
    def __init__(self, patient, doctor, date, time, status):
        self.appointment_id = appointment_id_no()
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time
        self.status = status
        self.appointments = []

#Generate appointment id number using random method
def appointment_id_no():
    return random.randint(13900, 159870)


class HospitalSystem:
    def __init__(self):
        self.patients = [] #List for storing registered patients
        self.doctors = []  #List for storing doctors information for profile viewing
        self.schedule = [] #List for storing doctor's schedule
        self.appointments = [] #List for storing appointments for patients
        self.billing = [] #list for storing billing information

#Register patients and storing data to patients[] list
    def register_patient(self):
        self.patients = []
        self.patient_id = patient_id_no()
        self.name = input("Enter patient's name")
        self.age = input("Enter age: ")
        self.gender = input("Enter gender : ")
        self.patients.append(f"Patients ID number : {patient_id_no()}")
        self.patients.append(f"Patients name : {self.name}")
        self.patients.append(f"Patients age : {self.age}")
        self.patients.append(f"Patients gender : {self.gender}")
        print("Patient was registered successfully!", self.patients)
        print(" ")

#Add medical doctors to hospital system using doctors list to store doctors information
    def add_doctors(self): #Adding doctors information to the system
        self.doctors = []
        self.name = input("Doctors name: ")
        self.age = input("Doctor's age: ")
        self.gender = input("Enter Doctors gender : ")
        self.speciality = input("Enter speciality: ")
        self.doctors.append(f"Doctor ID Number: {doctor_id_no()}")
        self.doctors.append(f"Doctor's name: {self.name}")
        self.doctors.append(f"Doctor's agee: {self.age}")
        self.doctors.append(f"Speciality: {self.speciality}")
        print(f"Doctors information:  {self.doctors}")
        print(f"Doctor {self.name} was successfully added to system")
        print(" ")
#viewing doctors profiles using print(self.doctors) to display doctors details
    def view_doctors_profile(self):
           print(self.doctors)

#viewing patients profile using print(self.patients) to display patients detail
    def view_patients_profile(self):
           print(self.patients)

# viewing schedule
    def view_schedule(self):
        print(self.schedule)

#
    def doctor_schedule(self): #adding doctors to schedule
       self.doctors_id = doctor_id_no()
       self.name = input("Doctors name: ")
       self.age = input("Doctor's age: ")
       self.gender = input("Doctors gender :")
       self.date = input("Available date in the format (23/2/2025): ")
       self.time = input("Enter time: (10:00am)")
       self.schedule.append(f"doctor ID Number: {doctor_id_no()}")
       self.schedule.append(f"Doctor's name: {self.name}")
       self.schedule.append(f"Doctor's age: {self.age}")
       self.schedule.append(f"Doctor's age: {self.gender}")
       self.schedule.append(f"Available date: {self.date}")
       self.schedule.append(f"Time: {self.time}")
       print(self.schedule)



    def books_appointment(self):
        self.status = "Successful"
        self.appointment_id = appointment_id_no()
        self.patient = input("Patients name: ")
        self.doctor = input("Doctor's name: ")
        self.date = input("Enter date(23/2/2025): ")
        self.time = input("Enter time: (10:00am)")
        self.appointments.append(f"Appointment ID Number: {appointment_id_no()}")
        self.appointments.append(f"Patient's name: {self.patient}")
        self.appointments.append(f"Doctor's name: {self.doctor}")
        self.appointments.append(f"Appointment date: {self.date}")
        self.appointments.append(f"Time: {self.time}")
        print(f"Appointments: {self.appointments}")
        print(f"Appointment status: {self.status}")


    def is_available(self):
          self.available_doctor = input("Enter Doctors name:")
          self.available_date = input("Enter date : ")
          self.available_time = input("Enter time: ")
          if self.available_doctor and self.available_date and self.available_time in self.schedule:
              print(f"This doctor is available for {self.available_date} at {self.available_time}: ")
          else:
             print(f"{self.available_doctor} is not available for {self.available_date} and {self.available_time}")

    def confirm_appointment(self):
        print("Do you want to proceed with your appointment? Answer: yes or no")
        self.response = input("Enter response: ")
        while True:
          if self.response == "yes":
             print("Appointment confirmed")
             break
          elif self.response == "no":
             self.cancel = input("Enter appointment id number : ")
          try:
             del self.appointments[0:4]
             print("Appointment has been cancelled successfully.")
             print(self.appointments)
             break
          except ValueError:
             print("Invalid appointment id number")




    def cancel_appointment(self):
             print(self.appointments)

             self.cancel_info = input("Enter appointment id number : ")
             if self.cancel_info in self.appointments:
                self.appointments.remove(self.cancel_info)
                print("Appointment has been cancelled successfully.")
             else:
                print("Invalid appointment id number")
                print(self.appointments)


    def receipt_no(self):
        return random.randint(1, 150)


    def generate_bill(self):
        pass
        while True:
          print("Health Plus Medical Care")
          print(".....Billing options........... ")
          print("consultation")
          print("injection")
          print("surgery")
          print("labs")
          print("exit")
          print(" ")


          self.name = input("Enter patient's name : ")
          self.date = input("Enter date: ")
          procedure = input("Enter procedure done: ")
          cost = int(input("Enter procedure cost: "))
          self.billing.append(self.name)
          self.billing.append(self.date)
          self.billing.append(procedure)
          self.billing.append(cost)
          option = "yes or no"

          print("Do you want to add more procedures?", option)
          choice = str(input())

          if choice == "yes":
             procedure_two = input("Enter procedure done: ")
             additional_procedure_cost = input("Enter cost of additional procedure: ")
             total_cost = int(cost) + int(additional_procedure_cost)
             self.billing.append(procedure_two)
             self.billing.append(additional_procedure_cost)
             self.billing.append(total_cost)
             print("Bill generated successfully")
             print(self.billing)
             print(self.receipt_generation())
             print(" ")
             break

          elif choice == "no":
              total_cost = int(cost)
              self.billing.append(total_cost)
              print(self.receipt())
              print(" ")
              break
          elif procedure == "exit":
              print("Exiting billing")
              break
          else:
               print("Thank you. Goodbye")



    def receipt_generation(self):
              print(".....Right Health Medical..........")
              print("...214 Spanish Avenue, Kingston....")
              print(".......Tel:876-345-9870............")
              print("..........Receipt..................")
              print(" ")
              print(f"Receipt number : {self.receipt_no()}")
              print(f"Patient's name:  {self.billing[0]}")
              print(f"Date: {self.billing[1]}")
              print(f"Procedure done:  {self. billing[2]}")
              print(f"Procedure fee:  {self. billing[3]}")
              print(f"Additional procedure: {self.billing[4]}")
              print(f"Additional procedure fee:  {self. billing[5]}")
              print(f"Total cost:  {self.billing[6]}")
              print("Thank you")
              print(" ")

    def receipt(self):
              print(".....Right Health Medical..........")
              print("...214 Spanish Avenue, Kingston....")
              print(".......Tel:876-345-9870............")
              print("..........Receipt..................")
              print(" ")
              print(f"Receipt number : {self.receipt_no()}")
              print(f"Patient's name:  {self.billing[0]}")
              print(f"Date: {self.billing[1]}")
              print(f"Procedure done:  {self.billing[2]}")
              print(f"Procedure fee:  {self.billing[3]}")
              print(f"Total cost:  {self.billing[4]}")
# ............................................................................................................
# ............Menu............................................................................................



def main_menu() :
 system = HospitalSystem()
 while  True:
    print("Right Health Hospital Management System")
    print("......214 Spanish Avenue, Kingston.....")
    print("..........Tel:876-345-9870.............")
    print(".............Menu......................")
    print("registration")
    print("patients profile")
    print("add doctor")
    print("doctors profile")
    print("patient appointment")
    print("doctors schedule")
    print("available doctors")
    print("billing")
    print("cancel appointment")
    print(" ")

    option = input("Enter menu options : ")


    if option == "registration": #working register patients and adds to information to system
         system.register_patient()

    elif option == "patient profile": #view patients profile from list
           system.view_patients_profile()

    elif option == "add doctor":
         system.add_doctors()  #working adds doctor to medical system

    elif option == "doctors profile": #view doctors profile from doctors list
          system.view_doctors_profile()

    elif option == "patient appointment": #booking appointment for patients
         system.books_appointment()
         system.confirm_appointment()

    elif option == "doctors schedule": #schedule doctors available dates for appointment
         system.doctor_schedule()
         

    elif option == "available doctors": #genderate billing information for patients
         system.view_schedule()
         system.is_available()

    elif option == "billing": #genderate billing information for patients
         system.generate_bill()

    elif option == "cancel appointment" : #removing appointment from list using remove() method
         system.cancel_appointment()

    else:
         print("try again")
# ..............Exception handling.............................................................

if __name__ == "__main__":
    main_menu()