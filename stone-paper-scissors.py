import random

userWins = 0
cpuWins = 0
drawMatches = 0

gameChoices = ['stone', 'paper', 'scissors']

cpuChoice = random.choice(gameChoices)

print("cpu choice is " + cpuChoice)

while True:
    userChoice = input("Enter your choice: ")
    print("user choice is " + userChoice)

    validChoice = False
    for i in gameChoices:
        if userChoice == i:
            validChoice = True

    # if validChoice == True:
    #     print("Choice is valid")
    #     break
    # else:
    #     userChoice = input("Please enter a valid choice: ")

    if userChoice in gameChoices:        #  in -> membership operator
        print("Valid choice")
        break
    else:
        print("Invalid choice")

if userChoice == cpuChoice:
    print("Game draw")

if userChoice == "stone":
    if cpuChoice == "paper":
        print("User lost")
    else:
        print("User won")

elif userChoice == "paper":
    if cpuChoice == "stone":
        print("User won")
    else:
        print("User lost")
else:
    if cpuChoice == "stone":
        print("User lost")
    elif cpuChoice == "paper":
        print("User won")
