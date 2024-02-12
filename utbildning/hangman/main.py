
import replit
import random
from hangman_art import stages 
from hangman_words import word_list 
from hangman_art import logo 

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
print(logo)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    replit.clear()

    if guess in display:
      print(f"You've already guessed this letter correctly {guess}")
    
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_word:        
        print(f"You guessed {guess} which is not in the word, you lose 1 life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])