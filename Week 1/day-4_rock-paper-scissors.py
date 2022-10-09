import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

gestures = [rock, paper, scissors]

choice = int(input('What do you choose? Type 0 for rock, 1 for paper or 2 for scissors\n'))

if choice > 2:
  print('Invalid input. You lose.')

else:
  print('You chose:')
  print(gestures[choice])
  
  
  sys_choice = random.randint(0,2)
  print('Your opponent chose:')
  print(gestures[sys_choice])
  
  print()
  
  if (choice == 0 and sys_choice == 2):
    print('You win!')
  
  elif choice == sys_choice:
    print('Draw')
  
  elif choice < sys_choice or (choice == 2 and sys_choice == 0):
    print('You lose. Better luck next time.')
  
  else:
    print('You win!')