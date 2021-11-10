import random
import datetime
from customer import Customer

id = 1234

atm = Customer(id)

while True:
    id = int(input('Enter your PIN: '))
    attempt = 0

    while id != int(atm.checkPIN()) and attempt < 3:
        id = int(input('Wrong PIN! Please enter your PIN again: '))
        attempt += 1

        if attempt == 3:
            print('Program error! Please take your card out and try again..')
            exit()

    while True:
        print('Welcome to Progate ATM..')
        print('\n1 - Check Balance \t 2 - Withdraw \t 3 - Deposit \t 4 - Change PIN \t 5 - Exit')

        menu = int(input('\nPlease select the menu: '))

        if menu == 1:
            balance = atm.checkBalance()
            print('\nYour balance: Rp ' + str(balance) + '\n')

        elif menu == 2:
            nominal = float(input('\nEnter your nominal: '))
            verify = input('Confirmation: Do you wish to withdraw your money with the nominal below? y/n \nRp ' + str(nominal) + "\n")

            if verify == "y":
                print('\nYour initial balance: Rp ' + str(atm.checkBalance()) + '\n')
            else:
                print('\nTransaction canceled!\n')
                break

            if (nominal < atm.checkBalance()):
                atm.withdraw(nominal)
                print('Transaction success!')
                print('Your remaining balance: Rp ' + str(atm.checkBalance()) + '\n')

            else:
                print('Sorry, your balance is not enough for withdrawal!')
                print('Please deposit your money into your account!\n')

        elif menu == 3:
            nominal = float(input('\nEnter your nominal: '))
            verify = input('Confirmation: Do you wish to deposit your money with the nominal below? y/n \nRp ' + str(nominal) + "\n")

            if verify == "y":
                atm.deposit(nominal)
                print('\nYour current balance: Rp ' + str(atm.checkBalance()) + '\n')
            else:
                print('\nTransaction canceled!\n')
                break
        
        elif menu == 4:
            currentPIN = int(input('\nEnter your current PIN: '))

            while currentPIN != atm.checkPIN():
                currentPIN = int(input('Wrong PIN! Please re-enter your PIN: '))

            newPIN = int(input('Enter your new PIN: '))

            print('\nYour PIN has been renewed..')

            verifyNewPIN = int(input('\nConfirmation: Enter your new PIN: '))

            if newPIN == verifyNewPIN:
                print('Success!\n')
            else:
                print('Wrong PIN number!\n')
        
        elif menu == 5:
            recordNumber = random.randint(100000, 1000000)
            date = datetime.datetime.now()
            remainingBalance = atm.checkBalance()

            print('\nThis receipt is automatically generated when you exit.\nPlease keep this receipt as a proof of your transaction.\n')
            print('Record No. #' + str(recordNumber))
            print('Date: ' + str(date))
            print('Remaining balance: ' + str(remainingBalance))
            print('Thank you for using Progate ATM!')
            exit()

        else:
            print('\nError. Sorry, this menu is unavailable..\n')