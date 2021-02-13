import random

# request user enter name
name = input("Please enter your name: ")
# welcome user to game
print("Welcome " + str(name) + " the dice is rolling")
print("You need to choose a number and if you choose the right number you win!")
# determine random number between 1 and 100 and number of dice roll between 1 and 6
random_number = random.randint(0, 101)
guesses = random.randint(1, 6)

# display number of guesses to user
for num in range(guesses):
    if guesses == 1:
        print("You have " + str(guesses) + " chance to play")
    else:
        print("You have " + str(guesses) + " chances to play")
# ask user to enter their choice of number
    yourGuess = int(input("Please enter a number of your choice: "))
    if yourGuess > 101:
        print("You lose a turn")
    elif yourGuess == random_number:
        print("You win!")
    elif yourGuess < random_number:
        print("Too low!")
    else:
        print("Too high!")
    if guesses == 1:
        print("You lose game over")
    elif guesses == 2:
        print(input("Please enter your second number: "))
        if yourGuess == random_number:
            print("You win!")
        else:
            print("You lose game over")
    elif guesses == 3:
        print(input("Please enter your second number: "))
        if yourGuess == random_number:
            print("You win!")
        elif yourGuess < random_number:
            print("Too low!")
            print(input("Please enter your third number: "))
            if yourGuess == random_number:
                print("You win!")
            else:
                print("You lose game over")
        elif yourGuess > random_number:
            print("Too high!")
            print(input("Please enter your third number: "))
            if yourGuess == random_number:
                print("You win!")
            else:
                print("You lose game over")
    elif guesses == 4:
        print(input("Please enter your second number: "))
        if yourGuess == random_number:
            print("You win!")
        elif yourGuess < random_number:
            print("Too low!")
            print(input("Please enter your third number: "))
            if yourGuess == random_number:
                print("You win!")
            elif yourGuess < random_number:
                print("Too low!")
                print(input("Please enter your fourth number: "))
                if yourGuess == random_number:
                    print("You win!")
                else:
                    print("You lose game over")
            elif yourGuess > random_number:
                print("Too high!")
                print(input("Please enter your fourth number: "))
                if yourGuess == random_number:
                    print("You win!")
                else:
                    print("You lose game over")
        elif yourGuess > random_number:
            print("Too high!")
            print(input("Please enter your third number: "))
            if yourGuess == random_number:
                print("You win!")
            elif yourGuess < random_number:
                print("Too low!")
                print(input("Please enter your fourth number: "))
                if yourGuess == random_number:
                    print("You win!")
                else:
                    print("You lose game over")
            elif yourGuess > random_number:
                print("Too high!")
                print(input("Please enter your fourth number: "))
                if yourGuess == random_number:
                    print("You win!")
                else:
                    print("You lose game over")
    elif guesses == 5:
        print(input("Please enter your second number: "))
        if yourGuess == random_number:
            print("You win!")
        elif yourGuess < random_number:
            print("Too low!")
            print(input("Please enter your third number: "))
            if yourGuess == random_number:
                print("You win!")
            elif yourGuess < random_number:
                print("Too low!")
                print(input("Please enter your fourth number: "))
                if yourGuess == random_number:
                    print("You win!")
                elif yourGuess < random_number:
                    print("Too low!")
                    print(input("Please enter your fifth number: "))
                    if yourGuess == random_number:
                        print("You win!")
                    else:
                        print("You lose game over")
                elif yourGuess > random_number:
                    print("Too high!")
                    print(input("Please enter your fifth number: "))
                    if yourGuess == random_number:
                        print("You win!")
                    else:
                        print("You lose game over")
            elif yourGuess < random_number:
                print("Too high!")
                print(input("Please enter your fourth number: "))
                if yourGuess == random_number:
                    print("You win!")
                elif yourGuess < random_number:
                    print("Too low!")
                    print(input("Please enter your fifth number: "))
                    if yourGuess == random_number:
                        print("You win!")
                    else:
                        print("You lose game over")
                elif yourGuess > random_number:
                    print("Too high!")
                    print(input("Please enter your fifth number: "))
                    if yourGuess == random_number:
                        print("You win!")
                    else:
                        print("You lose game over")
        elif yourGuess > random_number:
            print("Too high!")
            print(input("Please enter your third number: "))
            if yourGuess == random_number:
                print("You win!")
            elif yourGuess < random_number:
                print("Too low!")
                print(input("Please enter your fourth number: "))
                if yourGuess == random_number:
                    print("You win!")
                elif yourGuess < random_number:
                    print("Too low!")
                    print(input("Please enter your fifth number: "))
                    if yourGuess == random_number:
                        print("You win!")
                    else:
                        print("You lose game over")
                elif yourGuess > random_number:
                    print("Too high!")
                    print(input("Please enter your fifth number: "))
                    if yourGuess == random_number:
                        print("You win!")
                    else:
                        print("You lose game over")
            elif yourGuess > random_number:
                print("Too high!")
                print(input("Please enter your fourth number: "))
                if yourGuess == random_number:
                    print("You win!")
                elif yourGuess < random_number:
                    print("Too low!")
                    print(input("Please enter your fifth number: "))
                    if yourGuess == random_number:
                        print("You win!")
                    else:
                        print("You lose game over")
                elif yourGuess > random_number:
                    print("Too high!")
                    print(input("Please enter your fifth number: "))
                    if yourGuess == random_number:
                        print("You win!")
                    else:
                        print("You lose game over")
    elif guesses == 6:
        print(input("Please enter your second number: "))
        if yourGuess == random_number:
            print("You win!")
        elif yourGuess < random_number:
            print("Too low!")
            print(input("Please enter your third number: "))
            if yourGuess == random_number:
                print("You win!")
            elif yourGuess < random_number:
                print("Too low!")
                print(input("Please enter your fourth number: "))
                if yourGuess == random_number:
                    print("You win!")
                elif yourGuess < random_number:
                    print("Too low")
                    print(input("Please enter your fifth number: "))
                    if yourGuess == random_number:
                        print("You win!")
                    elif yourGuess < random_number:
                        print("Too low")
                        print(input("Please enter your last number: "))
                        if yourGuess == random_number:
                            print("You win!")
                        else:
                            print("You lose game over")
                    elif yourGuess > random_number:
                        print("Too high!")
                        print(input("Please enter your last number: "))
                        if yourGuess == random_number:
                            print("You win!")
                        else:
                            print("You lose game over")
                elif yourGuess > random_number:
                    print("Too high")
                    print(input("Please enter your fifth number: "))
                    if yourGuess == random_number:
                        print("You win!")
                    elif yourGuess < random_number:
                        print("Too low")
                        print(input("Please enter your last number: "))
                        if yourGuess == random_number:
                            print("You win!")
                        else:
                            print("You lose game over")
                    elif yourGuess > random_number:
                        print("Too high!")
                        print(input("Please enter your last number: "))
                        if yourGuess == random_number:
                            print("You win!")
                        else:
                            print("You lose game over")
            elif yourGuess > random_number:
                print("Too low!")
                print(input("Please enter your fourth number: "))
                if yourGuess == random_number:
                    print("You win!")
                elif yourGuess < random_number:
                    print("Too low")
                    print(input("Please enter your fifth number: "))
                    if yourGuess == random_number:
                        print("You win!")
                    elif yourGuess < random_number:
                        print("Too low")
                        print(input("Please enter your last number: "))
                        if yourGuess == random_number:
                            print("You win!")
                        else:
                            print("You lose game over")
                    elif yourGuess > random_number:
                        print("Too high!")
                        print(input("Please enter your last number: "))
                        if yourGuess == random_number:
                            print("You win!")
                        else:
                            print("You lose game over")
                elif yourGuess > random_number:
                    print("Too high")
                    print(input("Please enter your fifth number: "))
                    if yourGuess == random_number:
                        print("You win!")
                    elif yourGuess < random_number:
                        print("Too low")
                        print(input("Please enter your last number: "))
                        if yourGuess == random_number:
                            print("You win!")
                        else:
                            print("You lose game over")
                    elif yourGuess > random_number:
                        print("Too high!")
                        print(input("Please enter your last number: "))
                        if yourGuess == random_number:
                            print("You win!")
                        else:
                            print("You lose game over")
        elif yourGuess > random_number:
            print("Too high!")
            print(input("Please enter your third number: "))
            if yourGuess == random_number:
                print("You win!")
            elif yourGuess < random_number:
                print("Too low!")
                print(input("Please enter your fourth number: "))
                if yourGuess == random_number:
                    print("You win!")
                elif yourGuess < random_number:
                    print("Too low")
                    print(input("Please enter your fifth number: "))
                    if yourGuess == random_number:
                        print("You win!")
                    elif yourGuess < random_number:
                        print("Too low")
                        print(input("Please enter your last number: "))
                        if yourGuess == random_number:
                            print("You win!")
                        else:
                            print("You lose game over")
                    elif yourGuess > random_number:
                        print("Too high!")
                        print(input("Please enter your last number: "))
                        if yourGuess == random_number:
                            print("You win!")
                        else:
                            print("You lose game over")
                elif yourGuess > random_number:
                    print("Too high")
                    print(input("Please enter your fifth number: "))
                    if yourGuess == random_number:
                        print("You win!")
                    elif yourGuess < random_number:
                        print("Too low")
                        print(input("Please enter your last number: "))
                        if yourGuess == random_number:
                            print("You win!")
                        else:
                            print("You lose game over")
                    elif yourGuess > random_number:
                        print("Too high!")
                        print(input("Please enter your last number: "))
                        if yourGuess == random_number:
                            print("You win!")
                        else:
                            print("You lose game over")
            elif yourGuess > random_number:
                print("Too low!")
                print(input("Please enter your fourth number: "))
                if yourGuess == random_number:
                    print("You win!")
                elif yourGuess < random_number:
                    print("Too low")
                    print(input("Please enter your fifth number: "))
                    if yourGuess == random_number:
                        print("You win!")
                    elif yourGuess < random_number:
                        print("Too low")
                        print(input("Please enter your last number: "))
                        if yourGuess == random_number:
                            print("You win!")
                        else:
                            print("You lose game over")
                    elif yourGuess > random_number:
                        print("Too high!")
                        print(input("Please enter your last number: "))
                        if yourGuess == random_number:
                            print("You win!")
                        else:
                            print("You lose game over")
                elif yourGuess > random_number:
                    print("Too high")
                    print(input("Please enter your fifth number: "))
                    if yourGuess == random_number:
                        print("You win!")
                    elif yourGuess < random_number:
                        print("Too low")
                        print(input("Please enter your last number: "))
                        if yourGuess == random_number:
                            print("You win!")
                        else:
                            print("You lose game over")
                    elif yourGuess > random_number:
                        print("Too high!")
                        print(input("Please enter your last number: "))
                        if yourGuess == random_number:
                            print("You win!")
                        else:
                            print("You lose game over")
    break

# display game results to text file
statisticsFile = "statistics.txt"
# open text file
writeFile = open(statisticsFile, "a")
result = "You win!"
numAttempts = guesses
numAttempts += 0
for win in result:
    if numAttempts == result:
        writeFile.write(name + " | win | " + str(numAttempts))
    else:
        writeFile.write(name + " | loss | " + str(numAttempts))
    break
# close text file
writeFile.close()