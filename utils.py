# utils.py
from person import Person
from bank_account import BankAccount

def person_data():
    name = input("Enter the person's name:\n")
    new_person = Person(name)
    
    done = False
    while not done:
        acc_num = int(input("Enter a 4-digit account number:\n"))
        balance = float(input("Enter the initial balance:\n"))
        
        # Crear cuenta y agregarla a la persona
        account = BankAccount(acc_num, balance)
        new_person.add_account(account)
        
        choice = input("Are you done adding accounts? (yes/no):\n").lower()
        if choice == "yes":
            done = True
            
    return new_person

def balance_summary(person_list):
    for person in person_list:
        total_balance = sum(acc.balance for acc in person.accounts)
        print(f"{person.name} : {total_balance:.2f}")