import random

global firstNumber
global secondNumber
firstNumber = 1
secondNumber = 101
# numbers for customs guess range

uName = input(' \n Hello, before we continue, please enter a username. : ')
# username

yesList = ["y", "Y", "yes", "Yes", "YES", "sure", "ok"]
# lists to assist in determining what the user is trying to say in terms of confirmation

guess = int()
# the users guess


print(f' \n Great! Welcome to numberGuesser.py {uName}, this is a python script that allows you to guess numbers!')

#defining the main setion so i can refer to it later if the user wants to retry
def main():

    firstNumber = 1
    secondNumber = 101
    gCount = 0

    #declaring variables

    while True: #loop so users can make decisions to leave or continue
        rangeCheck = input(
            ' \n Would you like to select the range of numbers you want to guess? Otherwise you can default with 1 to 100. (Y/N) : ')

        if rangeCheck not in yesList:
            break

        else:
            while True:
                try: #using try to sanitise inputs, there's probably a better way of doing this
                    firstNumber = int(input(
                        " \n What would you like the lowest possible number to be? e.g. (low number - highest number) : "))

                except ValueError:
                    print(" \n Input Denied!")
                    continue

                else:
                    try:
                        secondNumber = int(input(" \n What would you like the highest possible number to be? e.g. (low number - highest number) : "))

                    except ValueError:
                        print(" \n Input Denied!")
                        continue

                guessCheck = input(
                    f' \n Nice, your number number guessing range should be between: \n \n   {firstNumber} and {secondNumber} \n \n If correct, type yes to begin guessing, if not, type no to reinsert your values. : ') #assisting in the ux incase my beloved users wrote the wrong numbers

                if guessCheck in yesList:
                    break

                else:
                    continue

            break

        break
# below is the actual number guessing part
    print(f" \n I'm thinking of a number between {firstNumber} and {secondNumber}, can you guess it?")

    try:
        cNum = random.randint(firstNumber, secondNumber)

    except ValueError:
        print(" \n Restarting guess section. Put in logical values you monkey!") #for any michevious users trying to break the guess process
        main()

    else:
        print(cNum)

        guess = ""

        while guess != cNum:
            try:
                guess = int(input(f" \n Guess a number between {firstNumber} and {secondNumber} : "))

            except ValueError:
                print(" \n Input denied!")
                continue

            else: #here are bunch of ifs to get responses depending on how close they are to number
                gCount = gCount + 1

                if guess == cNum: #here are if statements that check the users guess amount to give a comment based off of it
                    if gCount <= 10:
                        print(" \n You can do better than that!")
                    if gCount <= 6:
                        print(" \n Yeah alright mate, you've got some skill... or luck?")
                    if gCount <= 2:
                        print(" \n I think it's time to go get a lottery ticket!")
                    print(f' \n Congratulations! You took {gCount} guess(es) to get the right answer!')
                    break

                elif cNum > guess:
                    print(" \n You guessed too small!")

                elif cNum < guess:
                    print(" \n You Guessed too high!")

                else:
                    continue

        tAgain = input(" \n Again? (Y/N) : ")

        if tAgain in yesList:
            main()

        else:
            print(f" \n Thanks for playing {uName}! Have a wonderful rest of your day!")
            exit()

main()