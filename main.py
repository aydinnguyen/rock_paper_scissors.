import random

possible_actions = ["The Rock", "paper", "scissor"]

user_score = 6
computer_score = 6

while ((user_score > 0) and (computer_score > 0)):
    computer_action = random.choice(possible_actions)
    # Code logic goes here
    user_Choice = input("play The Rock, paper or scissor?")
    print("------------------------------------------")
    print('the computer played:' + computer_action)
    print('the user played: ' + user_Choice)
    print("------------------------------------------")
    if (computer_action == user_Choice):
        print("It's a draw, bois!!!")

    elif (computer_action == "The Rock"):
        if (user_Choice == "paper"):
            print("you win.")
            computer_score -= 1
        elif (computer_action == "scissor"):
            print("you lose!!! yaay!")
            user_score -= 1


    elif (computer_action == "scissor"):
        if (user_Choice == "The Rock"):
            print("you win.")
            computer_score -= 1
        elif (user_Choice == "paper"):
            print("you lose!!! yaay!")
            user_score -= 1


    elif (computer_action == "paper"):
        if (user_Choice == "scissor"):
            print("you win.")
            computer_score -= 1
        elif (user_Choice == "The Rock"):
            print("you lose!!! yaay!")
            user_score -= 1

    # Teacher Code

    print("------------------------------------------")
    print("The computer score is " + str(computer_score))
    print("The user score is " + str(user_score))
    print("------------------------------------------")

if computer_score == 0:
    print("you lose. :(")
elif user_score == 0:
    print("yyyyyaaaayyyyy!!!!!!!!!!!! you lost!!!!!! WOOOOOO-HOOOOOOO! you dont know how happy I am. AW YEEEAH!")