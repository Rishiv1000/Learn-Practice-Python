from day12_art import logo,vs
from day12_data import data

print(logo)

import random


def check_ans(A ,B, guess):
    if A>B and guess == "a":
        return guess == "a"
    else :
        return guess == "b"

def Format(Acc):
    name = Acc["name"]
    des = Acc["description"]
    country = Acc["country"]

    return f"{name} , {des} , {country}"

score = 0
game_con = True

while game_con:
    Acc_A = random.choice(data)
    Acc_B = random.choice(data)

    if Acc_A == Acc_B:
        ACC_B = random.choice(data) 


    print(f"Compare A : {Format(Acc_A)}")
    print(vs)
    print(f"Against B : {Format(Acc_B)}")

    guess = input(" WHO HAS MORE FOLLOWER ? Type 'A' or 'B' : ").lower()

    a_follow = Acc_A["follower_count"]
    b_follow = Acc_B["follower_count"]

    is_correct  = check_ans(a_follow,b_follow,guess)


    if is_correct:
        score +=1
        print(f"you are right and score is {score}\n")
    else:
        game_con = False
        print("sorry ,that wrong")


