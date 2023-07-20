import random
import hangman_art
import hangman_words
import os 
from hangman_words import word_list
from hangman_art import stages

chosen_word = random.choice(word_list)
empty_list = []
for _ in range(len(chosen_word)):
    empty_list.append('_')

endflag = True
lives = 6

print(hangman_art.logo)
while(endflag):
    guess = input("Please Guess a letter: ").lower()
    os.system('cls' if os.name == 'nt' else 'clear')
    index = 0
    for letter in chosen_word:
        if letter == guess:
            empty_list[index] = letter
        index += 1
    
    if guess not in chosen_word:
        print("You lose a life")
        lives -= 1
        
    
    if lives == 0:
        print(stages[0])
        print("You Lose")
        print(f"The word was {chosen_word}")
        endflag = False
        break
    
    if '_' not in empty_list:
        print("Congrats you won")
        endflag = False

    print(f"lives left: {lives}")
    print(stages[lives]) 
    print(empty_list)