# Task 1 
input_year = int(input ("Input year and I will tell you if it is a leap year: "))

if (input_year % 4 == 0 and input_year % 100 != 0) or (input_year % 400 == 0):
     print(str (input_year) + " is a leap year")
else: 
     print("The number entered is not a leap year.")