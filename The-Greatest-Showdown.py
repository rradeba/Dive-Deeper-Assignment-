# Task 1 
 number_one = int(input("What is the first number: "))
                 
number_two = int(input("What is a different second number: "))

number_three = int(input("What is the third number: "))
                                  
if ((number_one > number_two) and (number_one > number_three)):
    print("The first number is the greatest.")
elif ((number_two > number_one) and (number_two > number_three)):
    print("The second number is the greatest.")
elif ((number_three > number_one) and (number_three > number_two)):
    print("The third number is the greatest.")
else:
    print("Two or more of the numbers are the same or iinput is not an integer")

# Task 2 

number_one = int(input("What is the first number: "))
                 
number_two = int(input("What is a different second number: "))

number_three = int(input("What is a different third number: "))
                                  
if ((number_one > number_two) and (number_one > number_three)):
    print("The first number is the greatest.")
elif ((number_two > number_one) and (number_two > number_three)):
    print("The second number is the greatest.")
elif ((number_three > number_one) and (number_three > number_two)):
    print("The third number is the greatest.")
else:  
    print("Two or more of the numbers are the same or input is not an integer")

if ((number_one < number_two) and (number_one < number_three)):
    print("The first number is the least.")
elif ((number_two < number_one) and (number_two < number_three)):
    print("The second number is the least.")
elif ((number_three < number_one) and (number_three < number_two)):
    print("The third number is the least.")
else:
    print("Two or more of the numbers are the same or input is not an integer") 

#Task 3 

number_one = int(input("What is the first number: "))
                 
number_two = int(input("What is a second number: "))

number_three = int(input("What is a third number: "))

if ((number_one == number_two) and (number_one > number_three)):
    print("The smallest number is: " + str(number_three) + ". The largest number is: " + str(number_one) + ". Number one and number two are equal.")
elif ((number_two == number_three) and (number_two > number_one)):
    print("The smallest number is: " + str(number_one) + ". The largest number is: " + str(number_three) + ". Number two and number three are equal.")
elif ((number_three == number_one) and (number_three > number_two)):
    print("The smallest number is: " + str(number_two) + ". The largest number is: " + str(number_three) + ". Number one and number three are equal.")
elif ((number_one == number_two) and (number_one < number_three)):
    print("The smallest number is: " + str(number_one) + ". The largest number is: " + str(number_three) + ". Number one and number two are equal.")
elif ((number_two == number_three) and (number_two < number_one)):
    print("The smallest number is: " + str(number_two) + ". The largest number is: " + str(number_one) + ". Number two and number three are equal.")
elif ((number_three == number_one) and (number_three < number_two)):
    print("The smallest number is: " + str(number_three) + ". The largest number is: " + str(number_two) + ". Number one and number three are equal.")
elif ((number_one > number_two) and (number_one > number_three)):
    print("The first number is the greatest.")
elif ((number_two > number_one) and (number_two > number_three)):
    print("The second number is the greatest.")
elif ((number_three > number_one) and (number_three > number_two)):
    print("The third number is the greatest.")
elif ((number_one < number_two) and (number_one < number_three)):
    print("The first number is the least.")
elif ((number_two < number_one) and (number_two < number_three)):
    print("The second number is the least.")
elif ((number_three < number_one) and (number_three < number_two)):
    print("The third number is the least.")
else:
    print("The input is not an integer")