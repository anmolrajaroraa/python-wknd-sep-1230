import random

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


if userChoice == "stone":
    if cpuChoice == "stone":
        print("Game draw")
    elif cpuChoice == "paper":
        print("User lost")
    else:
        print("User won")

elif userChoice == "paper":
    pass
else:
    pass
