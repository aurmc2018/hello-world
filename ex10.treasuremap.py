import time

row1 = ['⚽','⚽','⚽']
row2 = ['⚽','⚽','⚽']
row3 = ['⚽','⚽','⚽']
items = [row1,row2,row3]

print("Treasure map game")
time.sleep(0.60)
print("In below there is a treasure hidden.")
time.sleep(0.60)
print("Guess the treasure to win")
time.sleep(0.60)
print(f"{row1}\n{row2}\n{row3}")
time.sleep(0.60)

coordinates = input("Where is the Treasure(Mention Column# and Row# as '12')> ")
verticle_position = int(coordinates[0])
horizontal_position = int(coordinates[1])
print(f"Verticle position is {verticle_position}")
time.sleep(0.55)
print(f"Horizontal position is {horizontal_position}")
items[verticle_position-1][horizontal_position - 1] = "X"
time.sleep(1)
# print(items)
print(f"{row1}\n{row2}\n{row3}")
time.sleep(0.2)
if coordinates == "11":
    print("Sako..!!! You got the Treasure. 🥳 🎉 🎉 🎊 ​🎶​")
else:
    print("Sorry 😞 !! You hit the wrong place. Better luck next time.")

