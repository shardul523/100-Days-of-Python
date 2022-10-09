import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

allCharacters = [letters, numbers, symbols]

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#Easy Level

# password = ''

# for l in range(0, nr_letters):
#   choice = random.randint(0, len(letters))
#   password += letters[choice]

# for s in range(0, nr_symbols):
#   choice = random.randint(0, len(symbols))
#   password += symbols[choice]

# for n in range(0, nr_numbers):
#   choice = random.randint(0, len(numbers))
#   password += numbers[choice]

# print('Your newly generated password is:',password)

password_characters = []
password_length = nr_letters + nr_symbols +nr_numbers

for l in range(0, nr_letters):
  choice = random.randint(0, len(letters))
  password_characters.append(letters[choice])

for s in range(0, nr_symbols):
  choice = random.randint(0, len(symbols))
  password_characters.append(symbols[choice])

for n in range(0, nr_numbers):
  choice = random.randint(0, len(numbers))
  password_characters.append(numbers[choice])

#Shuffling a list
random.shuffle(password_characters)

password = ''
for char in password_characters:
  password += char

print('Your newly generated password is:',password)