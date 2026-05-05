from person import Person
from bank_account import BankAccount
import utils

def main():
    people = []

    while True:
        print("\nChoose an option:")
        print("1. Add a new person")
        print("2. Add an account to a person")
        print("3. Show all balances")
        print("4. Quit")
        
        option = input()

        if option == "1":
            new_person = utils.person_data()
            people.append(new_person)

        elif option == "2":
            target_name = input("Enter the person's name:\n")
            # Buscar a la persona en la lista
            found_person = next((p for p in people if p.name == target_name), None)
            
            if found_person:
                acc_num = int(input("Enter a 4-digit account number:\n"))
                balance = float(input("Enter the initial balance:\n"))
                found_person.add_account(BankAccount(acc_num, balance))
            else:
                print("Person not found.")

        elif option == "3":
            if not people:
                print("No data to show.")
            else:
                utils.balance_summary(people)

        elif option == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1-4.")

if __name__ == "__main__":
    main()

