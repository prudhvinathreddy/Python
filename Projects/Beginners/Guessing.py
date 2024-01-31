import random
import math

print("================================\n| WELCOME TO THE GUESSING GAME |\n================================")
print()
min_range = int(input('Enter the min range value - '))
max_range = int(input('Enter max range value - '))
guessing_number = random.randint(min_range,max_range)
print("==============================================\n| I have a number in my mind - START GUESSING |\n==============================================")

count = 0
chances = round(math.log(max_range-min_range+1,2))
print("\nYou have only ", chances,  "chances to guess the number..!")

while count<chances:
  count+=1
  guess = int(input("\nGuess a number - "))

  if guessing_number == guess:
    print(" Woah...! You Did It")
    break
  elif guessing_number > guess:
    print("You guessed value is too small..! \nTRY AGAIN..!\nYou only have ", 
          chances-count , "chances")
  elif guessing_number < guess:
    print("You guessed value is too high..! \nTRY AGAIN..!\nYou only have ", chances-count , "chances")
    
if count>chances:
  print("\nThe number is ",guessing_number)
  print("\tBETTER LUCK NEXT TIME!")
