import random
def guessNumber():
  attempts = 0
  
  while True:
        try:
            num = random.randint(1, 100)
            attempts += 1
            guessedNumber = int(input("""
                            Welcome to the Number Guessing Game!
                            Try to guess the number between 1 and 100.
                            
 Enter your guess: """))
            if guessedNumber > num:
                print("Too high!")
            elif guessedNumber < num:
                print("Too low!")
            elif guessedNumber == num:
                print(f"Congratulations! You've guessed the number in {attempts} attempts.")
                break
        except KeyboardInterrupt:
            print("You have close this game")
            break
        except ValueError:
            print("Give a valid number")
    
guessNumber()