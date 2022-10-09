from replit import clear
import random
import hangman_art
# from hangman_art import logo, stages
# import hangman_words
from hangman_words import word_list

print(hangman_art.logo)

lives = 6 #len(stages)-1
lives_lost = 0

chosen_word = random.choice(word_list)

guessed_word = []

for _ in chosen_word:
  guessed_word += '_'

end_of_game = False

while end_of_game != True:
  
  letter_guess = input('Guess a letter: ').lower()
  clear()
  if letter_guess in chosen_word:
    if letter_guess in guessed_word:
      print(f"You have already guessed {letter_guess}")
    else:
      for index in range(len(chosen_word)):
        if chosen_word[index] == letter_guess:
          guessed_word[index] = letter_guess

    print(' '.join(guessed_word))

  else:
    print(' '.join(guessed_word))
    lives_lost += 1
    print(f"You guessed {letter_guess}, that's not in the word. You lose a life")
  
  print(hangman_art.stages[lives_lost])

  if lives == lives_lost or not ('_' in guessed_word):
    end_of_game = True



if lives == lives_lost:
  print('You lose')
  print(f'The correct word was {chosen_word}')

else:
  print('You win')