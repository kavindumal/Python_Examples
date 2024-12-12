# Simple contact management system
# 1. Requirments
#   Create a program that store and manage contacts in a file name contacts.txt
#   Each contact should have a name, phone number and email address.
# 2. Feature to implement
#   - View all contact (Read and display all contact from the file)
#   - Add a new contact (Append the contact to the file)
#   - Exit from the program.
# 3. Structure of the file
#   John Doe, 1234567890, John@Exmple.com
#   Jane Noe, 1234567890, Jane@Example.com

def show_menu():
    print('1. View all contacts')
    print('2. Add a new contact')
    print('3. Exit')
    choice = input('Enter your choice: ')
    return choice

def show_all_contacts():
    with open('file_example/file_writing/contacts.txt', 'r') as file:
        contacts = file.readlines()
        for contact in contacts:
            print(contact)

def add_new_contact():
    name = input('Enter name: ')
    phone = input('Enter phone: ')
    email = input('Enter email: ')
    with open('file_example/file_writing/contacts.txt', 'a') as file:
        file.write(f'{name}, {phone}, {email}\n')
    print('Contact added successfully.')
    
def main():
    while True:
        choice = show_menu()
        if choice == '1':
            show_all_contacts()
        elif choice == '2':
            add_new_contact()
        elif choice == '3':
            break
        else:
            print('Invalid choice. Please try again.')
            
if __name__ == '__main__':
    main()