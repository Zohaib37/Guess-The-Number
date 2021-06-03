import random
print("Welcome to the number guessing game!\nI'm thinking of a number between 1 and 100.")
random_number = random.randint(1, 100)

difficulty = ""
while difficulty != "easy" and difficulty != "hard":
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard'. ").lower()

lives = {
  "easy": 10,
  "hard": 5
}

num_lives = lives[difficulty] 

end_of_game = False

while not end_of_game:
  print(f"You have {num_lives} lives left.")
  user_number = int(input("Guess a number: "))
  if user_number == random_number:
    print("You win!")
    end_of_game = True
  elif user_number < random_number:
    print("Too low")
    num_lives -= 1
  else:
    print("Too high")
    num_lives -= 1
  if num_lives == 0:
    print(f"You lose, the number was: {random_number}")
    end_of_game = True



