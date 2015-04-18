# christopher_salazar_Lab2.py
# Name: Christopher Salazar
# Date: 02/09/2015
# This program will allow user to convert U.S Standard measurements to Metric.
# This program utilizes functions.
# This program uses if statements.

# Define Global Variables
MILES_TO_KM=1.6
GALLONS_TO_LITERS=3.9
POUNDS_TO_KILOGRAMS=0.45
INCHES_TO_CENTIMETERS=2.54

print("This program will convert U.S. Standard measurements into Metric measurements.")

# Main function

def main():
    "This is the main function."
    # Define Local Variables
    number_of_miles=0.0
    number_of_fah=0.0
    number_of_gallons=0.0
    number_of_pounds=0.0
    number_of_inches=0.0
    
    #MILES TO KM
    print('We will now convert Miles to Kilometers.\n')

    # Get miles from user
    number_of_miles= float(input('Enter the distance in Miles: '))

    # Validate input
    if number_of_miles<0.0:
        print('\n\n\n\nInput is invalid...\n\n\n\n')
        exit()
        
    # Convert and display result
    milesToKilometers(number_of_miles)
    

    #FAHRENHEIT TO CELCIUS
    print('We will now convert Fahrenheit to Celcius.\n')

    # Get Temperature from user
    number_of_fah= float(input('Enter the temperature in Fahrenheit: '))

    #Validate input
    if number_of_fah>1000.0:
        print('\n\n\n\nInvalid input. Please enter a value below 1000.0 F\n\n\n\n')
        exit()
        
    #Convert and display
    fahrenheitToCelsius(number_of_fah)
    

    #GALLONS TO LITERS
    print('We will now convert Gallons to Liters.\n')

    #Get gallons from user
    number_of_gallons= float(input('Enter the amount in Gallons: '))

    #Validate input
    if number_of_gallons<0:
        print('\n\n\n\nInput is invalid...\n\n\n\n')
        exit()
        
    #Convert and display
    gallonsToLiters(number_of_gallons)


    #POUNDS TO KILOGRAMS
    print('We will now convert Pounds to Kilograms.\n')

    #Get pounds from user
    number_of_pounds= float(input('Enter the amount in Pounds: '))

    #Validate input
    if number_of_pounds<0:
        print('\n\n\n\nInput is invalid...\n\n\n\n')
        exit()

    #Convert and display
    poundsToKilograms(number_of_pounds)


    #INCHES TO CENTIMETERS
    print('We will now convert Inches to Centimeters.\n')

    #Get Inches from user
    number_of_inches= float(input('Enter the length in Inches: '))

    #Validate input
    if number_of_inches<0.0:
        print('\n\n\n\nInput is invalid...\n\n\n\n')
        exit()

    #Convert and Display
    inchesToCentimeters(number_of_inches)

    #End Program Statement
    print('Thank you for using my program!! :)')

#MILES TO KM FUNCTION
def milesToKilometers(miles):
    "This function converts miles to km"
    #Declare local variables
    kilometers=0.0

    #Calculate number of Kilometers
    kilometers=miles * MILES_TO_KM

    #Display number in KM
    print ("The conversion of", format(miles, '.2f'), "Miles", end=' ')
    print ("to Kilometers is", format(kilometers, '.2f'), "KM.\n")

#FAHRENHEIT TO CELCIUS
def fahrenheitToCelsius(fah):
    "This function converts Fahrenheit to Celcius"
    #Declare local variables
    celsius=0.0

    #Calculate conversion
    celsius=(fah - 32) * (5/9)

    #Display in Celcius
    print ("The conversion of", format(fah, '.2f'), "Fahrenheit", end=' ')
    print ("to Celcius is", format(celsius, '.2f'), "C.\n")

#GALLONS TO LITERS
def gallonsToLiters(gal):
    "This function converts Gallons to Liters"
    #Declare local variables
    liters=0.0

    #Calculate
    liters= gal * GALLONS_TO_LITERS

    #Display
    print ("The conversion of", format(gal, '.2f'), "Gallons", end=' ')
    print ("to Liters is", format(liters, '.2f'), "Liters.\n")

#POUNDS TO KILOGRAMS
def poundsToKilograms(pounds):
    "This function converts Pounds to Kilograms"
    #Declare local variables
    kilograms=0.0

    #Calculate
    kilograms= pounds * POUNDS_TO_KILOGRAMS

    #Display
    print ("The conversion of", format(pounds, '.2f'), "LBS", end=' ')
    print ("to Kilograms is", format(kilograms, '.2f'), "KG.\n")

#INCHES TO CENTIMETERS
def inchesToCentimeters(inches):
    "This function converts inches to centimeters"
    #Declare local variables
    centimeters=0.0

    #Calculate
    centimeters= inches * INCHES_TO_CENTIMETERS

    #Display
    print ("The conversion of", format(inches, '.2f'), "Inches", end=' ')
    print ("to Centimeters is", format(centimeters, '.2f'), "cm.\n")    

#Call the main function
main()
