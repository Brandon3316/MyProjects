#Temperature converter
#The while will keep the user repeatedly in entering what temperture to choose a integer to covert
#It will keep asking the user until the user types quit which exits the program
while True:
    temperature = input("(C)elsius, (F)ahrenheit or type quit: ")
    if temperature == "C":
        #The var variables act like enter and exit keys for the user
        #If the user enters a letter, the user will be propt to try again by entering an integer
        #var = 0 is the enter key var = 1 is the exit key
        var = 0
        while var == 0:
            fahrenheit = input("Enter fahrenheit to convert: ")
            try:
            #The equation converts fahrenheit to celsius
                fahrenheit = int(fahrenheit)
                celsius = (fahrenheit - 32) / 1.8
                print(celsius)
                #User will not leave until a integer is entered
                var = 1
            #The ValueError exception will prevent to program from crashing
            except ValueError:
                print("Invalid, please enter an integer: ")
#It works the same way from the fahrenhiet to to celsius conversion
    elif temperature == "F":
        var = 0
        while var == 0:
            celsius = input("Enter celsius to convert: ")
            try:
            #This equation converts from celsius to fahrenheit
                celsius = int(celsius)
                fahrenheit = (celsius * 1.8) + 32
                print(fahrenheit)
                var = 1
            except ValueError:
                print("Invalid, please enter an integer: ")
#The user can type quit to exit the program
    elif temperature == "quit":
        break
#This prevent to program from crashing and prompts the user to enter the correct input
    else:
        print("Invalid")