import random

def guess_number_game():
     secret_number = random.randint(0, 100)
     lives = 5

     print("Welcome to the Number Guessing Game!")
     print("Guess a number between 0 and 100.")

     while lives > 0:
          user_guess = int(input("Your guess: "))

          if user_guess == secret_number:
               print("Congratulations! You guessed the correct number.")
               break
          elif user_guess < secret_number:
               print("Your guess is lower than the number. Try again!")
          else:
               print("Your guess is higher than the number. Try again!")

          lives -= 1
          print(f"You have {lives} lives remaining.")

     if lives == 0:
          print(
              f"Sorry, you're out of lives. The correct number was {secret_number}."
          )

# Run the game
guess_number_game()
