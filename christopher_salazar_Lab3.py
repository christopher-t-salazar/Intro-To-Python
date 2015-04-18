# christopher_salazar_lab3.py
# Name: Christopher Salazar
# Date: 02/12/2015
# This program will calculate whether employee earns commission and bonus based on sales and time of service.


# Global Variables
baseSalary=2000

# Main function
def main():
    "This is the main function for the program"
    #Local Variables
    sales=0.0
    months=0
    comRate=0.0 #Commission Rate
    paycheck=0.0
    bonus=0.0
    addedBonus=0.0
    vacDays=0
    deduction=0.0
    
    print('This program calculates and displays an itemized \nmonthly paycheck for the Salesperson.\n\n')

    salesman= input('Enter the Salesperson\'s name: ')

    sales= float(input('Enter the Salesperson\'s total sales this month: '))

    months= int(input('Enter the number of months Salesperson has been with company: '))

    vacDays= float(input('Enter the number of Vacation days Salesperson took this month: '))
    
    # Calculating Commission
    if sales>=10000 and sales<=100000:
        comRate= sales * .02
    elif sales>100000 and sales<=500000:
        comRate= sales * .15
    elif sales>500000 and sales<=1000000:
        comRate= sales * .28
    elif sales>1000000:
        comRate= sales * .35
    else:
        comRate=0.0
        
    #Calculate Bonus
    if months>=3 and sales>100000 and sales<=500000:
        bonus=1000
    elif months>=3 and sales>500000 and sales<=1000000:
        bonus=5000
    elif months>=3 and sales>1000000:
        bonus=100000
    else:
        bonus=0.0

    #Calculate 5 year bonus 
    if months>=60 and sales>100000:
        addedBonus=1000
    else:
        addedBonus=0.0

    #Calculate deduction
    if vacDays>3:
        deduction=-200
    else:
        deduction=0.0

    #Calculate Pay
    paycheck= baseSalary + comRate + bonus + addedBonus + deduction

    #Display Results
    print('\n\n\n\nName of Salesperson:',salesman,'\n')
    print('Length of time with SoftwareXYZ Inc.:',months, \
          'months.','\n')
    print('Number of vacation days taken this month:',vacDays,'\n')
    print('Base Salary: $',format(baseSalary, ',.2f'), \
          '\n',sep='')
    print('Commission earned: $',format(comRate, ',.2f'), \
          '\n',sep='')
    print('Bonus earned: $',format(bonus, ',.2f'),'\n', \
          sep='')
    print('Additional bonus earned:',format(addedBonus, ',.2f'), \
          '\n',sep='')
    print('Deductions:',format(deduction, '.2f'),'\n')
    print('Total Net Paycheck: $',format(paycheck, ',.2f'), \
          sep='')

    
main()
    
    
    
