enterCheck = 0
selectDVD = 0

# basic customer details

uName = ""
uSurname = ""
uAddress = ""
uID = ""

# payment customer details

uCreditNumber = ""
uCreditExpiry = ""
uCreditCVV = ""
uCreditType = ""

lDVD = "Rent Failed"

def main():
    print(
        " \n -=-=-=-= DAVID'S DVD RENTAL / =-=-=-=- \n 1. Select DVD \n 2. Inspect rental costs \n 3. Insert Customer Details \n 4. Purchase selected dvd with inserted payment & information \n 5. Exit  \n-=-=-=-= DAVID'S DVD RENTAL / =-=-=-=- \n ")

    while True:
        try:
            global enterCheck
            enterCheck = int(input("Please select an option (1-5) : "))
            if enterCheck > 5 or enterCheck < 1:
                print('Sorry, your response was not allowed.')
                continue

        except ValueError:
            print('Sorry, your response was not allowed.')
            continue

        else:
            break

    if enterCheck == 1:
        global lDVD
        print(" \n -=-=-=-= DAVID'S DVD RENTAL / Select DVD =-=-=-=- \n 1. DVD - locating clownfish \n 2. DVD - jndiana iones part 8 \n 3. DVD - mikael myers \n 4. DVD - screech 5 \n 5. DVD - trucks 2 \n 6. DVD - slow and calm \n-=-=-=-= DAVID'S DVD RENTAL / Select DVD =-=-=-=- \n ")
        selectDVD = int(input('Please select an option (1-6) : '))
        if selectDVD == 1:
            lDVD = "locating clownfish"
        elif selectDVD == 2:
            lDVD = "jndiana iones"
        elif selectDVD == 3:
            lDVD = "mikael myers"
        elif selectDVD == 4:
            lDVD = "screech 5"
        elif selectDVD == 5:
            lDVD = "trucks 2"
        elif selectDVD == 5:
            lDVD = "slow and calm"

        print(" \n Selection stored, returning user to main. \n ")
        main()

    if enterCheck == 2:
        print(" \n -=-=-=-= DAVID'S DVD RENTAL / Inspect rental costs =-=-=-=- \n 1. DVD - locating clownfish - €5 per fortnite \n 2. DVD - jndiana iones part 8 - €2 per week \n 3. DVD - mikael myers €-3 per millennia \n 4. DVD - screech 5 - €0 per year \n 5. DVD - trucks 2 - €96 per second \n 6. DVD - slow and calm - €10 per 3 days \n-=-=-=-= DAVID'S DVD RENTAL / Inspect rental costs =-=-=-=- \n ")
        priceCheck = input("Type 'return' to return to main : ")
        while priceCheck != "return":
            priceCheck = input("Type 'return' to return to main : ")
        print(" \n Returning user to main. \n ")
        main()

    if enterCheck == 3:
        print(' \n Basic customer information. \n ')

        uName = input("What is your name? : ")
        print(f'Customer name: {uName}')
        uSurname = input("What is your surname? : ")
        print(f'Customer surname: {uSurname}')
        uAddress = input("What is your address? : ")
        print(f'Customer address: {uAddress}')
        uID = input("What is your ID number? : ")
        print(f'Customer ID: {uID}')

        print(' \n Now for payment details. \n ')

        uCreditNumber = input("What is your credit card number? : ")
        print(f'Customer credit card number: {uCreditNumber}')
        uCreditExpiry = input("What is your credit card expiry number? : ")
        print(f'Customer credit card expiry: {uCreditExpiry}')
        uCreditCVV = input("What is your credit card CVV? : ")
        print(f'Customer credit card CVV: {uCreditCVV}')
        uCreditType = input("What is your credit card type? : ")
        print(f'Customer credit card type: {uCreditType}')

        print(' \n Double Check your details before submitting. \n ')

        print(' \n  Your Basic  Information \n ')
        print(f'Name | {uName}')
        print(f'Surname | {uSurname}')
        print(f'Address | {uAddress}')
        print(f'User ID | {uID}')
        print(' \n  Your Payment Information \n ')
        print(f'Credit card number | {uCreditNumber}')
        print(f'Credit card expiry | {uCreditExpiry}')
        print(f'Credit card CVV | {uCreditCVV}')
        print(f'Credit card type | {uCreditType}')
        print(
            ' \n  If you want to change the information above, return to the main menu and re-enter your details. \n ')

        print(' \n -= Disclaimer =- \n  \n > inputting incorrect or outdated information can lead to failure in acquiring goods. \n ')
        aCheck = input("Type 'acknowledge' to acknowledge this information and return to main : ")
        while aCheck != "acknowledge":
            aCheck = input("Type 'acknowledge' to acknowledge this information and return to main : ")
        print("Returning user to main.")
        main()

    if enterCheck == 4:
        if lDVD != "Rent Failed":
            print(f" \n You have rented {lDVD}! Enjoy the movie! \n \n Don't forget to return it! \n ")
            exit()
        else:
            print(' \n Rent Failed')
            main()

    if enterCheck == 5:
            print(' \n Terminating program alongside any submitted details.')
            exit()

main()