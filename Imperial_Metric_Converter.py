#Imperial Metric Weight converter

#This project is in progress
#The features need to be added such as inputing keys and functions
#for the progam not to crash from an imputing mistake by the user
while True:
    weight = float(input("Weight: "))
    unit = input("(K)g or (L)bs: ")
    if unit.upper() == "K":
        converted = weight / 0.45
        print("Weight in Lbs:" + str(converted))
    elif unit.upper() == "L":
        converted = weight * 0.45
        print("Weight in Kg: " + str(converted))
    elif unit.upper() == "quit":
        break
    else:
        print("Invalid")

