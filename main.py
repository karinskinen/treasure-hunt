print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

left_right = input("Would you like to go left or right ? ")
lower_left_right = left_right.lower()
if lower_left_right == "left":
  swim_wait = input("It was a wise choice to make. Let's see if you'll survive the next step.\n You're now on an island and you want to get to the main land.\n You could either wait for a boat or swim by yourself. \n Do you want to swim or wait for the boat? ")
  lower_swim_wait = swim_wait.lower()
  if lower_swim_wait == "wait":
    print("Wow, now I'm getting impressed by you. The treasure is close, I can feel it. ")
    print("You're now in a room with three doors.")
    chosen_door = input("Which door do you want to explore? Red, Blue or Yellow? ")
    lower_chosen_door = chosen_door.lower()
    if lower_chosen_door == "red":
      print("You went trough the door without looking and burned in a fire of lava.\n Game over!")
    elif lower_chosen_door == "blue":
      print("Yummy, yummy in a giant beast tummy. Game over!")
    elif lower_chosen_door == "yellow":
      print("WOW, you are amazing! You win and take all the treasure with you!")
    else:
      print("Game over!")
  else:
    print("You weren't as lucky this time. Luigi stept on your head and you died.. Game over!")
else :
  print("The big aligator came from nowhere and ate your head. Game over!")


