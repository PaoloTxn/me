"""Week 3, Exercise 3

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    
    isnumber = 0
    
    print("\nWelcome to the guessing game!")

    while isnumber == 0:   
      upperBound = get_good_number("Enter an upper bound: ")
      lowerBound = get_good_number("Enter an lower bound: ")
      if upperBound < 1:
        print("lower or equal to 1")
      elif lowerBound >= upperBound:
        print(f"{lowerBound} {upperBound} Range needs to be lower")
        x = lowerBound
        lowerBound = upperBound
        upperBound = x
        isnumber = 1
      else:
        isnumber = 1

    print(f"OK then, a number between {lowerBound}" + f" and {upperBound} ?")
    actualNumber = random.randint(lowerBound, upperBound)
    print(f"actualnumber {actualNumber}")

    while isnumber == 1:
      guessedNumber = input("Now guess a number between the range!: ")
      try:
        guessedNumber = int(guessedNumber)
        if guessedNumber > upperBound or guessedNumber < lowerBound:
          print("OUTSIDE THE BOUNDS CHOOSE AGAIN")
        else:
          print(f"You guessed {guessedNumber}")
          if guessedNumber == actualNumber:
            print("You got it!! It was {}".format(actualNumber))
            return "You got it!"
            isnumber = 0
          elif guessedNumber < actualNumber:
            print("Too small, try again :'(")
          else:
            print("Too big, try again :'(")
        
      except:
        print("This is not a valid number")

def get_good_number(message):
  while True:
    inputnum = input(message)
    try:
      inputnum = int(inputnum)
      return inputnum
    except:
      print(f"{inputnum} This is not a valid number")
  
    

    # while not guessed:
    #     guessedNumber = int(input("Guess a number: "))
    #     print("You guessed {},".format(guessedNumber),)
    #     if guessedNumber == actualNumber:
    #         print("You got it!! It was {}".format(actualNumber))
    #         guessed = True
    #     elif guessedNumber < actualNumber:
    #         print("Too small, try again :'(")
    #     else:
    #         print("Too big, try again :'(")
    # return "You got it!"

    # the tests are looking for the exact string "You got it!". Don't modify that!


if __name__ == "__main__":
    print(advancedGuessingGame())
