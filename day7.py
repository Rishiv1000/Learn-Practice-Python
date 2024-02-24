import random

stage = [ """

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",  """

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""", """

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""" , """

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""","""

  +---+
  |   |
  O   |
  |   |
      |
      |
=========""","""

  +---+
  |   |
  O   |
      |
      |
      |
=========""",
"""
   +---+
   |   |
       |
       |
       |
       |
========="""]



word_list = ["apple","banana","orange"]
word = random.choice(word_list)
print(f"this is {word}")

lives = 6

test_list = []
blank = '_'
for i in range(len(word)):
    test_list.append(blank)
print(test_list)
 

listofword = list(word)
while not test_list == listofword :
    letter = str(input("Guess the Letter\n")).lower()
    for i in range(len(word)):
        if word[i] == letter: 
            test_list[i] = letter 
    print(test_list)     
    if letter not in word_list:
        lives-=1
        if lives == 0:
            print("You loose")
            break

    if test_list == listofword:
        print("won")      
   
    print(stage[lives])
# print(test_list)




