# christopher_salazar_Lab9.py
# Name: Christopher Salazar
# Date: 04/15/2015
# This program will store and recall user created e-mail lists.



# Import Module
import pickle

# Main function
def main():
    user_choice=0
    em=start_up()   
    while user_choice!=9:
        user_choice=main_menu()
        if user_choice==1:
            look_up(em)
        elif user_choice==2:
            enter_new(em)
        elif user_choice==3:
            change_email(em)
        elif user_choice==4:
            delete_email(em)
    save_data(em)
    print('Program will now end..')


#Function populates the main menu and allows user input.
def main_menu():
    print('\nWelcome to the E-mail Database.  Please select from the following options:\n')
    print('~~~~~Main Menu~~~~~')
    print('1. Look up personel e-mail address.')
    print('2. Add new name and e-mail address.')
    print('3. Change/Update existing e-mail.')
    print('4. Delete e-mail address.')
    print('9. Quit Program')
    try:
        user_choice=int(input('\nEnter selection: '))
        while user_choice<1 or user_choice>5 and user_choice!=9:
           user_choice=int(input('\nInvalid Entry. Please Enter selection again: '))
        return user_choice
    except ValueError:
        print('Main Menu Value Error')


# Retrive and unpickle
def start_up():
    try:
        input_file=open('emailroster.dat', 'rb')
        email=pickle.load(input_file)
        input_file.close()
        return email 
    except IOError:
        print('IO')
        email={}
        return email
    except EOFError:
        print('EOFE')
        email={}
        return email

#Function runs a search for a name.    
def look_up(em):
    again='Y'
    name=input("Enter person's name for search: ")

    print(name + "'s email address is: " + em.get(name, 'Not Found.'))
    while again=='Y':        
        again=input('Enter a person\'s name for search? Y for YES, N for NO: ').upper()
        if again=='Y' or again=='YES':
            name=input("Enter person's name for search: ")
            print(name + "'s email address is: " + em.get(name, 'Not Found.'))
        else:
            again='N'
            

#Function allows new entries to be added.            
def enter_new(em):
    again='Y'
    
    while again=='Y':
        name= input('Enter person\'s name: ')
            
        if name not in em:
            email_address=input('Enter person\'s e-mail address: ')
            em[name]=email_address
        else:
            print('Entry already exists.\n')
        again=input('Add another entry? Y for YES. N for NO.: ').upper()
    save_data(em)


#Function allows exisiting email to be changed.    
def change_email(em):
    again='Y'    
    while again=='Y':
        name= input('Enter person\'s name: ')            
        if name in em:
            email_address=input('Enter person\'s new e-mail address: ')
            em[name]=email_address
        else:
            print('\''+name+'\''+' is not found.\n')
        again=input('Change another entry? Y for YES. N for NO.: ').upper()
    save_data(em)

#Function allows deletion of email on record.
def delete_email(em):
    again='Y'    
    while again=='Y':
        name= input('Enter person\'s name to delete: ')   
        if name in em:
            del em[name]
            print(name,'has been deleted.')
        else:
            print('Name is not found.\n')
        again=input('Delete another entry? Y for YES. N for NO.: ').upper()
    save_data(em)

#Save/Pickle file
def save_data(em):
    try:
        output_file=open('emailroster.dat', 'wb')
        pickle.dump(em, output_file)
        output_file.close()
    except IOError:
        print('Save Data IO Error')
    except EOFError:
        print('Save Data EOFError')

#Call Main Function
main()
