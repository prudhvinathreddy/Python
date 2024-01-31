import random
min_range = int(input('Enter the min range value - '))
max_range = int(input('Enter max range value - '))
guessing_number = random.randint(min_range,max_range)
count = 0
chances = round(math.log(upper-lower+1,2))
print("\n You have only ", chances,  "chances to guess the number..!\n")

while count<chances:
  count+=1
  guess = int(input("Guess a number - "))

  if guessing_number == guess:
    print(" Woah...! You Did It")
  elif guessing_number > guess:
    print("You guessed value is too small..! \n TRY AGAIN..! \n You only have ", 
          chances-count , "chances")
  elif guessing_number < guess:
    print("You guessed value is too high..! \n TRY AGAIN..! \n You only have ", 
          chances-count , "chances")
if count>=chances:
  print("\n The number is %d" % guessing_number)
  print(""\t BETTER LUCK NEXT TIME!")
