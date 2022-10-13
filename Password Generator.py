#Password Generator
import random


print("Password Generator: ")

#The shuffle definition is what helps to make the password generate random characters.
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

#Each of the letters, numbers, and symbols are generated according to the ASCII chart and each of the characters are randomly picked by the decimal ID.
uppercaseLetter1=chr(random.randint(65, 90))
uppercaseLetter2=chr(random.randint(65, 90))
lowercaseLetter1=chr(random.randint(97, 122))
lowercaseLetter2=chr(random.randint(97, 122))
digit1=chr(random.randint(48, 57))
digit2=chr(random.randint(48, 57))
punctuationSign1=chr(random.randint(32, 96))
punctuationSign2=chr(random.randint(32, 96))
punctuationSign3=chr(random.randint(32, 96))
punctuationSign4=chr(random.randint(32, 96))

#The password is added up by uppercase letters, lowercase letters, numbers, and symbols and they are in random order and not in a set for the password to be more secure.
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 + punctuationSign1 + punctuationSign2 + punctuationSign3 + punctuationSign4
password = shuffle(password)


print(password)