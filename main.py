'''
2. Exploring Python Modules and Data Structures Assignment

Objective:
The aim of this assignment is to deepen your understanding of Python modules, 
both built-in and custom, and to enhance your skills in working with various Python data structures like lists, 
dictionaries, and sets. This assignment focuses on practical applications of these concepts in real-world scenarios.

Task 1: Contact List Manager

Problem Statement: Create a Python script using a custom module to manage a contact list. 
The script should allow adding, removing, and displaying contacts stored in a list.
Code Example:
'''
import contacts_manager

def main():
    while True:
        print("\n1. Add a contact\n2. Remove a contact\n3. Display a contact\n4. Exit")
        choice = input("Enter an option: ")
        if choice == "1":
            name = input("Enter name.")
            phone = input("Enter phone.")
            email = input ("Enter email")
            contacts_manager.add_contact(name,phone,email)
        elif choice == "2":
            name = input("Enter name of contact to remove. ")
            contacts_manager.remove_contact(name)
        elif choice == "3":
            contacts_manager.display_contact()
        elif choice == "4":
            break
        else:
            print("Invalid choice please select from (1-4)")
if __name__ == "__main__":
    main()



