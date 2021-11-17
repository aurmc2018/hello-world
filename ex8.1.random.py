import random

print("Integer Random No. betwenn 1-5",random.randint(1,5))
print("Float Number between 0 - 5.0000",random.random() * 5)

heads_or_tails=input("Type heads or tales ")
print(heads_or_tails)
random_integer=random.randint(0,2)
print("Computer Guess", random_integer)
if random_integer == 1:
  print("Heads")
else:
  print("Tails")

if heads_or_tails== 1 and random_integer == 1:
  print("You win")
else:
  print("Computer wins")


