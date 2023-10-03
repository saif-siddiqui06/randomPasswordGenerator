import random


print("----------------------------------------------------------------")
# Define the character sets to use in the password
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
special_characters = '!@#$%^&*()'

# Combine the character sets into one string
all_characters = lowercase_letters + uppercase_letters + digits + special_characters

while True:
     # Get the length of the password from the user
     password_length = int(input("Enter the length of the password: "))
     if password_length == 0 :

          break
     else:
          # Generate the password
          password = ''
          for i in range(password_length):
               password += random.choice(all_characters)




          # Print the password
          print("Your password is:", password)
