import random
import time

word_list = ["apple", "banana","grapes"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(chosen_word)

display=[]
for _ in range(word_length):
    display +="_"

print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess a leter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
           display[position]= letter
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win.")

