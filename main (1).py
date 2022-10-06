import string
import random
#was questioning if I could write this better. One more thing is that not all of the special characters are included in this list.
alpha = list(string.ascii_letters)
digit = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


print("I AM THE FREE PASSWORD GENERATOR. USE ME TO CREATE A SECURE AND CUSTOMIZALE PASSWORD!The Program will take letters, digits, and special characters to create a password that has a customizable length.")

#takes characters, digits, special characters well
def generate_random_password():
  length = int(input("Enter the length of your password: "))
  alpha_count = int(input("Enter the alphabet count for your password: "))
  digit_count = int(input("Enter the digits count for your password: "))
  special_characters_count = int(input("Enter the special characters count for password:  "))
 # this is the length of the password. it works well too 
  characters_count = digit_count + special_characters_count + alpha_count
#this could have been written a bit better but still works fine.
  if characters_count > length:
    print(" The  total count of your characters exceeds the password length")
    return(1)
  password = []
  for i in range(alpha_count):
	  password.append(random.choice(alpha))
  for i in range(digit_count):
	  password.append(random.choice(digit))
  for i in range(special_characters_count):
	  password.append(random.choice(special_characters))
  if characters_count < length:
	  random.shuffle(characters)
  for i in range(length - characters_count):
   password.append(random.choice(characters))
   random.shuffle(password)
  print("".join(password))
#called the function. neccessary for def 
generate_random_password()

