print("ROCK PAPER SCISSOR")
while True:
    str1=("Rock","Paper","Scissor")
    user=input("Enter Your hand gesture: ")
    if user in str1:
        print(user)
    else:
        print("invalid string")
    import random 
    computer_choice=["Rock","Paper","Scissor"]
    choice=random.choice(computer_choice)
    print(choice)
    if user == "Rock" and choice == "Scissor":
        print("user is winner.")
    elif user == "Rock" and choice == "Paper":
        print("computer  is winner.")
    elif user == "Rock" and choice == "Rock":
        print("play again.")
    elif user == "Scissor" and choice == "Paper":
        print("user is winner.")
    elif user == "Scissor" and choice == "Scissor":
        print("play again.")
    elif user == "Scissor" and choice == "Rock":
        print("computer is winner.")
    elif user == "Paper" and choice == "Scissor":
        print("computer is winner.")
    elif user == "Paper" and choice == "Rock":
        print("user is winner.")
    elif user == "Paper" and choice == "Paper":
        print("user is winner.")
    play=input("Do you want to play again(yes/no)? : ")
    if play == "no":
        print("Game Ended!") 
        break

