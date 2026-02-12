# import and global variables
import random

USER_CHOICES = ("rock", "paper", "scissor")

# create a function to get user input
def get_user_input():
    choice = input("pick your choice (\"rock\", \"paper\", \"scissor\"): ")
    while choice not in USER_CHOICES:
        choice = input("pick your choice (\"rock\", \"paper\", \"scissor\"): ")
    return choice

# create a function to get pc input
def get_pc_input():
    pc_choice = random.choice(USER_CHOICES)
    print("pc choice was: ", pc_choice)
    return pc_choice

# compare and determine which one is the winner
def determine_winner(user_input, pc_input):
    if user_input == pc_input:
        print("Draw!")
    elif (user_input == "rock" and pc_input == "scissor") \
        or (user_input == "scissor" and pc_input == "paper") \
        or (user_input == "paper" and pc_input == "rock"):
        print("user won!")
    else:
        print("pc won!")
    

