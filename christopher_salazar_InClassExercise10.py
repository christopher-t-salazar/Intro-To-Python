# christopher_salazar_InClassExercise10.py
# Name: Christopher Salazar
# Date: 04/20/2015
# This contains 5 created student objects passed from the student class

# Import student module
import student

#Main Function
def main():
    #Get user input
    
    for x in range(1,6):
        print('\nEnter information for Student',x)
        stuNAME=input('Enter Student Name: ')
        stuID=input('Enter Student ID: ')
        stuGPA=input('Enter Student GPA: ')
        stuGRADE=input('Enter Student Expected Grade: ')
        stuTIME=input('Is student FULL-TIME or PART-TIME?')

    #Pass input into Class
        stuINFO=student.Student(stuNAME,stuID,stuGPA,stuGRADE,stuTIME)
        
    #Display output from Class
        print("\n~~~~Information Entered For Student",x)
        print('Student Name: ',stuINFO.get_name())
        print('Student ID: ', stuINFO.get_studentID())
        print('Student GPA: ',stuINFO.get_gpa())
        print('Student GRADE: ',stuINFO.get_grade())
        print('Student TIME STATUS: ', stuINFO.get_time())


#Call Main Function
main()
