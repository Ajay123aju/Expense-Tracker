import csv
from datetime import datetime
FILE_NAME = "expenses.csv"

def setup_file():
    try:
        with open(FILE_NAME, 'x',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date","Category","Amount","Note"])
    except FileExistsError:
        pass

def add_expense():
    date=datetime.now().strftime("%d-%m-%y")
    category=input("Enter Category(Food/Travel/Petrol/Shopping/Others:) ")
    amount = float(input("Enter amount : "))
    note = input("Enter note (optional): ")

    with open(FILE_NAME, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])
    
    print("✅ Expense added successfully!")

def view_expenses():
    with open(FILE_NAME, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def main():
    setup_file()
    while True:
        print("\n---Expense Tracker---")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Exit")
        choice = input("Enter Your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Exiting...")
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()