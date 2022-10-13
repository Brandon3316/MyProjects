#Feet and meters converter

#This project is in progress
#The features need to be added such as inputing keys and functions
#for the progam not to crash from an imputing mistake by the user
while True:
    unit = input("Feet or Meters: ")
    if unit == "Meters":
        while int():
            print("Please Enter Feet or Meters: ")
        else:
            feet = int(input("Enter feet: "))
            meters = feet * 0.304
            print(meters)
    elif unit == "Feet":
            meters = int(input("Enter meters: "))
            feet = meters * 3.28
            print(feet)
    elif unit == "quit":
        break
    else:
        print("Invalid")
