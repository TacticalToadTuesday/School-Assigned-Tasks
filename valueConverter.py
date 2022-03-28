import math


def FtoC(fahrenheit):  # fahrenheit to celsius
    return (fahrenheit - 32) * 5 / 9


def CtoF(celsius):  # celsius to fahrenheit
    return (celsius * (9/5)) + 32


def FtoM(feet):  # feet to metres
    return feet / 3.281


def MtoF(metres):  # metres to feet
    return metres * 3.281


def PtoK(pounds):  # pounds to kilos
    return pounds / 2.205


def KtoP(kilos):  # kilos to pounds
    return kilos * 2.205


sList = ["1", "2", "3", "4", "5", "6"]  # the user selection list "verification"


def main():  # define so i can easily restart the main script
    print(" \n -=-=-=-=-= CALEB'S CONVERTER =-=-=-=-=-")
    print(" \n 1. Fahrenheit - Celsius ")
    print(" \n 2. Celsius - Fahrenheit ")
    print(" \n 3. Metres - Feet ")
    print(" \n 4. Feet - Metres ")
    print(" \n 5. Kilograms - Pounds")
    print(" \n 6. Pounds - Kilograms")
    print(" \n -=-=-=-=-= CALEB'S CONVERTER =-=-=-=-=-")

    try:
        mSelect = input(" \n What would you like to convert today! (1-6) : ")  # initial menu input question
        if mSelect not in sList:  # kill if answer is invalid
            print(" \n Error, returning to main menu.")
            main()

    except ValueError:  # backup sanitization
        print(" \n Error, returning to main menu.")
        main()

    else:  # all r for calculating their respective values
        if mSelect == "1":
            uInput = float(input(" \n Initial value : "))

            eResult = FtoC(uInput)

            print(f" \n {uInput} Degrees Fahrenheit = {eResult} Degrees Celsius")

        if mSelect == "2":
            uInput = float(input(" \n Initial value : "))

            eResult = CtoF(uInput)

            print(f" \n {uInput} Degrees Celsius = {eResult} Degrees Fahrenheit")

        if mSelect == "3":
            uInput = float(input(" \n Initial value : "))

            eResult = MtoF(uInput)

            print(f" \n {uInput} Metres = {eResult} Feet")

        if mSelect == "4":
            uInput = float(input(" \n Initial value : "))

            eResult = FtoM(uInput)

            print(f" \n {uInput} Feet = {eResult} Metres")

        if mSelect == "5":
            uInput = float(input(" \n Initial value : "))

            eResult = KtoP(uInput)

            print(f" \n {uInput} Kilos = {eResult} Pounds")

        if mSelect == "6":
            uInput = float(input(" \n Initial value : "))

            eResult = PtoK(uInput)

            print(f" \n {uInput} Pounds = {eResult} Kilos")

        aVari = input(" \n Again? (Y/N) : ")
        if aVari in ["y", "Y", "yes", "Yes"]:  # replay
            main()

        else:
            print(" \n Goodbye, user. ")  # exit
            exit()

main()
