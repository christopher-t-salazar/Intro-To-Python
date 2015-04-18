# christopher_salazar_Lab8.py
# Name: Christopher Salazar
# Date: 04/12/2015
# This program will change date output into a long date format.

#global variables
longMonth=''
numeric_date=''
date_list=[]

#global constant
longYear=2015

#Main Function
def main():
    get_date()
    convertDATE()

# Grabs date from user and validates input.
def get_date():
    global date_list
    print('This program will convert a numeric date into long date format.\n')
    
    numeric_date=input('Enter a numeric date in the format of mm/dd/yy: ')
    date_list=numeric_date.split('/')
    date_list[0]=int(date_list[0])
    date_list[1]=int(date_list[1])
    date_list[2]=int(date_list[2])
    while date_list[0]>12 or date_list[0]<1: #Month Validation
        date_list[0]=int(input('Error: Month Input. Please enter a value between 01-12.'\
                               '\nEnter two digit Month: '))
    while date_list[1]>31 or date_list[1]<1: #Day Validation
        date_list[1]=int(input('Error: Day Input. Please enter a value between 01-31.'\
                               '\nEnter two digit Day: '))
    while date_list[2]!=15: # Year Validation
        date_list[2]=int(input('Error: Year Input.  Please enter "15" as the Year Value.'\
                               '\nEnter two digit Year: '))

#Converts the date into long date format and prints date.        
def convertDATE():
    global longMonth, date_list, longYear
    
    month_list=['January','February','March','April','May','June','July',
                'August','September','October','November','December']
    
    for x in range(date_list[0]):
        longMonth=month_list[x]

    print('\nYour inputted date converted to Long Date Format:\n')
    print(longMonth,date_list[1],',',longYear) # Long Date Format
    
main()



