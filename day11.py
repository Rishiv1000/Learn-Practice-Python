
import random 

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

target = random.randint(1,101)

print("Choose a difficulty.")
difficulty = input("Type 'easy' or 'hard: ")

point = 0
if difficulty == 'easy':
    point = 5
elif difficulty == 'hard':
    point = 10

for i in range(0, point):
    print(f"You have {point-i} attempts remaining to guess the number")
    print(f"Make a guess :")
    guess = int(input(""))
    if guess == target:
        print("You Win")
        break
    elif guess > target:
        print("Too high")
        if i < point:
            print("Guess Again")
        else:
            print("over chances are gone")
            break
    elif guess < target:
        print("Too low")
        if i < point:
            print("Guess Again")
        else:
            print("over chances are gone")
            break
      