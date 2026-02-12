# import function we need
from program import determine_winner, get_pc_input, get_user_input

# create the main function as the runner
def main():
    user_input = get_user_input()
    pc_input = get_pc_input()
    determine_winner(user_input, pc_input)
    print("end of this turn")

# make an iteration for doing the game as much as we need
answer = "y"
while answer =="y":
    main()
    answer = input("Do you want to coutinue? (y/n):")
