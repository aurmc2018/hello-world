import random
from hangman_art import stages, logo
from hangman_words import word_list

end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

        #If lives goes down to 0 then the game should stop and it should print "You lose."
        if lives  == 0:
            end_of_game = True
            print("You lose.")
    #Join all the elements in the list and turn it into a String.
    print(f"{'.'.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
    # print(f"lives={lives}")
    print(stages[lives])
    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.