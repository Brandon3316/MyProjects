#This will validate to see if the passwords are strong or weak (True or false respectively).
#This project is in progress and will be modified to properly detect the strong password instead of outputting false all the time to resolve the issue
import re

def isStrongPassword(password):

  if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[\w~@#$%^&*+]{8,}$", password):

    return True

  return False

#These strings contains various passwords for it to be validted to see if they are strong and secure, the weak ones will be false while the strong sppasswords are true.
print(isStrongPassword("abc"))

print(isStrongPassword("ABC"))

print(isStrongPassword("123"))

print(isStrongPassword("abcdefgh"))

print(isStrongPassword("abcdEFGH"))

print(isStrongPassword("12345678"))

print(isStrongPassword("abcd1234"))

print(isStrongPassword("ABCD1234"))

print(isStrongPassword("abcD1234"))

print(isStrongPassword("ebA5cBM9?re"))

print(isStrongPassword("a#B#c$1#2#3"))
