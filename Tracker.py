import csv
from collections import defaultdict
from datetime import datetime

FILE_NAME = "expenses.csv"

def get_date():
    today = datetime.now().strftime("%d-%m-%y")
    user_input = input(f"Enter Date [dd-mm-yy] default {today}): ").strip()

    if user_input == "":
        return today
    else:
        try:
            date_obj = datetime.strptime(user_input, "%d-%m-%y")
            return date_obj.strftime("%d-%m-%y")
        except ValueError:
            print("❌ Invalid date! Using today's date instead.")
            return today

def setup_file():
    try:
        with open(FILE_NAME, 'x',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date","Category","Amount","Note"])
    except FileExistsError:
        pass

def add_expense():
    date = get_date()
    category = input("Enter Category(Food/Travel/Petrol/Shopping/Others:) ").strip().title()

    try:
        amount = float(input("Enter amount : ").strip())
    except ValueError:
        print("❌ Invalid amount! Please enter a number.")
        return

    note = input("Enter note (optional): ").strip()
    if note == "":
        note = "No Note"

    with open(FILE_NAME, 'a', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, note])
    
    print("✅ Expense added successfully!")

def view_expenses():
    try:
            with open(FILE_NAME, 'r', encoding="utf-8") as file:
                reader = csv.reader(file)
                data = list(reader)

            if len(data) <= 1:
                print("\n⚠️ No expenses recorded yet!")
                return
            
            header = data[0]
            rows = data[1:]
            
            rows.sort(key=lambda x: datetime.strptime(x[0], "%d-%m-%y"))
            col_widths = [12, 15, 10, 20]
            
            print(f"{'Date':<{col_widths[0]}} | {'Category':<{col_widths[1]}} | {'Amount':<{col_widths[2]}} | {'Note':<{col_widths[3]}}")
            print("-" * (sum(col_widths) + 9))
            
            for row in rows:
                print(f"{row[0]:<{col_widths[0]}} | {row[1]:<{col_widths[1]}} | {row[2]:<{col_widths[2]}} | {row[3]:<{col_widths[3]}}")

    except FileNotFoundError:
        print("\n⚠️ No expense file found!")


def summary_report():
    try:
        with open(FILE_NAME, 'r', encoding="utf-8") as file:
                reader = csv.reader(file)
                data = list(reader)

        if len(data) <= 1:
                print("\n⚠️ No expenses recorded yet!")
                return
            
        rows = data[1:]

        total=0
        category_totals = defaultdict(float)
        highest_expense = ("",0,"","")

        for row in rows:
            date, category, amount, note = row
            amount = float(amount)
            total += amount
            category_totals[category] += amount
            
            if amount > highest_expense[1]:
                highest_expense = (date, amount, category, note)

        print("\n📊 --- Expense Summary ---")
        print(f"💰 Total Spent: {total:.2f}\n")

        print("📂 Spending by Category:")
        for cat, amt in category_totals.items():
            print(f"   - {cat:<12}: {amt:.2f}")

        print("\n🏆 Highest Expense:")
        print(f"   {highest_expense[1]:.2f} on {highest_expense[0]} ({highest_expense[2]}) - {highest_expense[3]}")

    except FileNotFoundError:
        print("\n⚠️ No expense file found!")

def main():
    setup_file()
    while True:
        print("\n---Expense Tracker---")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Summary Report") 
        print("4. Exit")
        choice = input("Enter Your choice: ")

        match choice:
            case "1": 
                add_expense()
            case "2":
                view_expenses()
            case "3":
                summary_report()
            case "4": 
                print("Exiting...") 
                break
            case _:
                print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()