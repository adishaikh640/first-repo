import webbrowser
from datetime import datetime
import time
# import webbrowser
a = "driving license"
b = a.upper()
c = b.center(50)
print(c.upper())
person1 = input("ENTER YOUR FIRST NAME")
person2 = input("ENTER YOUR MIDDLE NAME")
d = person2.center(5)
print(person1.upper()+d.upper())
def calculate_age(birthdate):
   birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
   today = datetime.now()
   age = today.year - birthdate.year - ((today.month, today.day) < 
 (birthdate.month, birthdate.day))
   return age
birthdate = input("Please enter your birthdate (YYYY-MM-DD): ")
# birthdate = input("Please enter your birthdate (YYYY-MM-DD): ")
year, month, day = map(int, birthdate.split('-'))
print("Year:", year)
print("Month:", month)
print("Day:", day)
age = calculate_age(birthdate)
print("You are", age, "years old.")
if age >= 18 or age <= 60:
  f = "You are eligible to get a driving license".upper()
  print(f)
  time.sleep(2)
  webbrowser.open('https://parivahan.gov.in/parivahan//en/content/driving-licence-0')
else:
  print("you are not eligible to get a driving license".upper())