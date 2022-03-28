import math


def add(num1, num2):  # addition
    return num1 + num2


def sub(num1, num2):  # subtraction
    return num1 - num2


def multi(num1, num2):  # multiplication
    return num1 * num2


def div(num1, num2):  # division
    return num1 + num2


def percent(num1, num2):  # percentage via num1 percent of num2
    return (num1 / num2) * 100

yesList = ["y", "Y", "yes", "Yes"]


selList = ["1", "2", "3", "4", "5", "6", "7"]

num1 = 0.0
num1 = 0.0


def main():
    print(" \n -=-=-=-= CALCULATOR =-=-=-=-")
    print(" \n 1. Insert your base two numbers to perform on. (default 0, 0)")
    print(" \n 2. Perform Addition on base two numbers. (num1 + num2) ")
    print(" 3. Perform Subtraction on base two numbers. (num1 - num2) ")
    print(" 4. Perform Multiplication on base two numbers. (num1 * num2) ")
    print(" 5. Perform Division on base two numbers. (num1 / num2) ")
    print(" 6. Perform Percent calculation on base two numbers. (num1 % num2) ")
    print(" \n 7. Use python eval function. ")
    print(" \n -=-=-=-= CALCULATOR =-=-=-=-")

    select = input(" \n Select option (1-7) : ")

    if select not in selList:
        print(" \n Input Invalid - Returning Main")
        main()

    else:

        if select == "1":

            while True:

                global num1

                try:
                    num1 = float(input(" \n First Number : "))

                except ValueError:
                    print(" \n Incorrect Value")
                    continue

                else:
                    break

            while True:

                global num2

                try:
                    num2 = float(input(" \n Second Number : "))

                except ValueError:
                    print(" \n Incorrect Value")
                    continue

                else:

                    print(" \n Numbers stored, returning to main menu!")

                    main()

        if select == "2":
            print(f" \n >>> ADDITION \n \n {num1} + {num2} = {add(num1, num2)}")

            input(" \n Press Enter to continue : ")

            main()

        if select == "3":
            print(f" \n >>> SUBTRACTION \n \n {num1} - {num2} = {sub(num1, num2)}")

            input(" \n Press Enter to continue : ")

            main()

        if select == "4":
            print(f" \n >>> MULTIPLICATION \n \n {num1} * {num2} = {multi(num1, num2)}")

            input(" \n Press Enter to continue : ")

            main()

        if select == "5":
            print(f" \n >>> DIVIDE \n \n {num1} / {num2} = {div(num1, num2)}")

            input(" \n Press Enter to continue : ")

            main()

        if select == "6":
            print(f" \n >>> PERCENTAGE \n \n {percent(num1, num2)}% makes up {num1} in {num2}")

            input(" \n Press Enter to continue : ")

            main()

        if select == "7":
            while True:
                print(f" \n >>> PYTHON EVAL")

                content = input(" \n >>> ")

                try:
                    result = eval(content)

                except(NameError, SyntaxError, ValueError):
                    print(" \n Error - Restarting Module")
                    continue



                else:
                    print(f" \n >>> {result}")

                    again = input(" \n Again? (Y/N) : ")

                    if again in yesList:
                        continue

                    else:
                        main()


main()
