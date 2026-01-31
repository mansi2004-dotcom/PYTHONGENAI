
print("ROCK PAPER SCISSOR")
user_win = 0
comp_win = 0
count = 0
match_draw = 0
while True:
    str1=("Rock","Paper","Scissor")
    user=input("Enter Your hand gesture: ")
    if user in str1:
        print(user)
    else:
        print("invalid string") 
    count += 1
    import random 
    computer_choice=["Rock","Paper","Scissor"]
    choice=random.choice(computer_choice)
    print(choice)
    if user == "Rock" and choice == "Scissor":
        print("user is winner.")
        user_win += 1
    elif user == "Rock" and choice == "Paper":
        print("computer  is winner.")
        comp_win += 1 
    elif user == "Rock" and choice == "Rock":
        print("Match is tie.")
        match_draw += 1
    elif user == "Scissor" and choice == "Paper":
        print("user is winner.")
        user_win += 1
    elif user == "Scissor" and choice == "Scissor":
        print("Match is tie.")
        match_draw += 1
    elif user == "Scissor" and choice == "Rock":
        print("computer is winner.")
        comp_win += 1 
    elif user == "Paper" and choice == "Scissor":
        print("computer is winner.")
        comp_win += 1 
    elif user == "Paper" and choice == "Rock":
        print("user is winner.")
        user_win += 1
    elif user == "Paper" and choice == "Paper":
        print("Match is tie.")
        match_draw += 1
    play=input("Do you want to play again(yes/no)? : ")
    if play == "no":
        print("Game Ended!") 
        break
print("You run the game",count,"times")
print("Computer wins: ",comp_win)
print("User wins: ",user_win)
print("Match draw: ",match_draw)
result = f"You run the game :{count}\n Computer wins:{comp_win}\n User wins:{user_win}\n Match draw : {match_draw}"

with open("file1.txt","w") as f:
    f.write(result)