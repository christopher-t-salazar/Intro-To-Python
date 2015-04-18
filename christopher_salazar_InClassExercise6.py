# christopher_salazar_InClassExercise6.py
# Name: Christopher Salazar
# Date: 03/09/2015
# This program simulates a vending machine.


#Global Constants

snickers=0.89
mms=1.39
kitkat=1.39
lays=0.50
doritos=0.50
cheetos=1.49
tictac=1.04
starburst=0.79
skittles=2.49

#Main function
def main():
    "Main function will call and incorporate other functions together."
    #Local Variables
    proceed=1
    choice=''
    price=0.0
    nameSnack=''
    while proceed==1: #loop will allow repeat in event of error/more purchases.
        print('Welcome to the Salazar Family Virtual Vending Machine!\n')

        display_menu()
        choice=choose(choice)
        
        print('\nYou choose Selection: ',choice)

        price=display_price(price,choice)
        
        print('Total Price: $',format(price, '.2f'))

        amountTendered(price)
        keep_going=int(input('\nThank you for using the Salazar \
Family Vending Machine!\nPress "1" to purchase another item, or "2" to quit: '))
        if keep_going==1:
            proceed=1
        else:
            proceed=0
def display_menu():
    print('\t\t|Menu|\t\t')
    print('-------------------------------------')
    print('-------------------------------------\n')
    print('Select\t\tSnack\t\tPrice')
    print('-------------------------------------\n')
    print('A1\t\tSnickers\t$0.89\n'\
          'A2\t\tM&Ms\t\t$1.39\n' \
          'A3\t\tKitKat\t\t$1.39\n')
    print('-------------------------------------')
    print('-------------------------------------\n')
    print('Select\t\tSnack\t\tPrice')
    print('-------------------------------------\n')
    print('B1\t\tLays\t\t$0.50\n' \
          'B2\t\tDoritos\t\t$0.50\n'\
          'B3\t\tCheetos\t\t$1.49\n')
    print('-------------------------------------')
    print('-------------------------------------\n')
    print('Select\t\tSnack\t\tPrice')
    print('-------------------------------------\n')
    print('C1\t\tTicTac\t\t$1.04\n'\
          'C2\t\tStarburst\t$0.79\n'
          'C3\t\tSkittles\t$2.49\n')

    
def choose(choice):
    keep_going='yes'
    
    while keep_going=='yes':
        choice=input('Please choose your snack based on the Select column: ')
        if choice == 'A1' or choice == 'A2' or choice == 'A3' \
           or choice == 'B1' or choice ==  'B2'  or choice == 'B3' \
           or choice == 'C1' or choice == 'C2' or choice == 'C3':
            keep_going=='no'
            return choice
        else:           
            print('Invalid entry: Please select from A1-C3\n')

def display_price(price, choice):
    if choice== 'A1':
        price=0.89
        return price
    elif choice == 'A2':
        price=1.39
        return price
    elif choice == 'A3':
        price=1.39
        return price
    elif choice == 'B1':
        price=0.50
        return price
    elif choice == 'B2':
        price=0.50
        return price
    elif choice == 'B3':
        price=1.49
        return price
    elif choice == 'C1':
        price=1.04
        return price
    elif choice== 'C2':
        price=0.79
        return price
    elif choice== 'C3':
        price=2.49
        return price
    else:
        print('Error: Program will end. Please Restart.')
        exit

def amountTendered(price):
    billAmount=0.0
    change=0.0
    keep_going='yes'

    while keep_going=='yes':
        billAmount=float(input('\nPlease enter bills now.  Machine accepts dollar increments up to $4.00 .\
\nEnter Bill Amount: '))
        if billAmount>=price and billAmount<=4.00:
            print('\nYou have entered: $',format(billAmount, '.2f'),'dollars.')
            change= billAmount-price
            print('\nYour selection and change will now be dispensed.\nChange Amount: $', format(change, '.2f'))
            keep_going='no'
        elif billAmount<price or billAmount>4.00:
            print('\nERROR: Insufficient Funds or Dollar increment exceeding $4.00.\nBills will be returned, please try again.\n')
main()

