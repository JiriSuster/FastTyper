import random


def play():
    choices = ["k","n","p"]
    computer = random.choice(choices)
    user = input("zadej k/n/p ")
    print("user: ", user)
    print("computer: ", computer)
    
    if computer == "k" and user == "p":
        return "you won"
    if computer == "n" and user == "k":
        return "you won"
    if computer == "p" and user == "n":
        return "you won"
    if computer == user:
        return "draw"
    return "you lose"