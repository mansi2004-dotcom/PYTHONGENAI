while True:
    comp=45
    user=int(input("Guess number: "))
    if comp == user:
        print("You Guess Right Number")
    else:
        print("Not a Correct Guess")
    choise=input("Do you want to guess number again(yes/no)?: ")
    if choise != "yes":
        print("Game Ended!!")
        break