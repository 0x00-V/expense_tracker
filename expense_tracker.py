import os
from os import system
import os.path
import datetime
import sqlite3
import matplotlib.pyplot as plt


try:
        try:
            sqliteConnection = sqlite3.connect('expenses.db')
            cursor = sqliteConnection.cursor()
        except sqlite3.Error as error:
            print('Error occured -', error)
            exit(1)


        def addExpense():
            system("clear||cls")
            date = "null"
            category = "null"
            description = "null"
            currency_symbol = "null"
            amount = "null"
            errmsg = ""
            while True:
                system("clear||cls")
                if errmsg != "":
                    if ("date" not in errmsg and "category" not in errmsg and "currency symbol" not in errmsg and "amount" not in errmsg):
                        ""
                    else:
                        print(errmsg,"\n")
                print("Expense Tracker - Add Expenses")
                print(f"\nDate: {date}\nCategory: {category}\nDescription: {description}\nCurrency: {currency_symbol}\nAmount: {amount}")
                print("\n\n1. Set Date\n2. Set Category\n3. Set Description\n4. Set Currency\n5. Set Amount\n\n6. Add Expenses\n7. Back\n8. Exit\n\n")
                user_option = input()
                system("clear||cls")
                match user_option:
                    case "1":
                        def getDate():
                            nonlocal errmsg
                            while True:
                                try:
                                    print("Expense Tracker - Add Expenses - Set Date")
                                    date_entry = input("Enter a date in YYYY-MM-DD format: ")
                                    year, month, day = map(int, date_entry.split('-'))
                                    date_input = datetime.date(year, month, day)
                                    if "date" in errmsg:
                                        errmsg = errmsg.replace("|date|", "")
                                    return date_input
                                except ValueError:
                                    system("clear||cls")
                                    print("Incorrect Date Format (Enter 0 to go back and set to null)")
                                    if date_entry == "0":
                                        return "null"     
                        date = getDate()
                        system("clear||cls")
                    case "2":
                        system("clear||cls")
                        print("Expense Tracker - Add Expenses - Set Category")
                        print("Select a Category\n\n1. Food & Groceries\n2. Transport\n3. Entertainment\n4. Utilities\n5. Shopping\n6. Health\n7. Subscriptions\n8. Other\n9. Back\n\n")
                        category_selection = input()
                        match category_selection:
                            case "1":
                                category = "Food & Groceries"
                                errmsg = errmsg.replace("|category|", "")
                            case "2":
                                category = "Transport"
                                errmsg = errmsg.replace("|category|", "")
                            case "3":
                                category = "Entertainment"
                                errmsg = errmsg.replace("|category|", "")
                            case "4":
                                category = 'Utilities'
                                errmsg = errmsg.replace("|category|", "")
                            case "5":
                                category = "Shopping"
                                errmsg = errmsg.replace("|category|", "")
                            case "6":
                                category = "Health"
                                errmsg = errmsg.replace("|category|", "")
                            case "7":
                                category = "Subscriptions"
                                errmsg = errmsg.replace("|category|", "")
                            case "8":
                                category = "Other"
                                errmsg = errmsg.replace("|category|", "")
                            case _:
                                category = "null"
                    case "3":
                        system("clear||cls")
                        print("Expense Tracker - Add Expenses - Set Description")
                        print(f"Set a description for your expense\n\nCurrent Description: {description}\n\nEnter your description: ")
                        description = input()
                        system("clear||cls")
                    case "4":
                            def getCurrencySymbol():
                                nonlocal errmsg
                                print("Expense Tracker - Add Expenses - Set Currency")
                                print("Set the currency you're using (e.g $, £, ¥)\n\nSymbol: ")
                                currency_input = input()
                                errmsg = errmsg.replace("|currency symbol|", "")
                                return currency_input
                            system("clear||cls")
                            currency_symbol = getCurrencySymbol()
                            while len(currency_symbol) > 1:
                                system("clear||cls")
                                print("Please only enter 1 character.")
                                currency_symbol = getCurrencySymbol()
                    case "5":
                        def getAmount():
                            nonlocal errmsg
                            while True:
                                print("Expense Tracker - Add Expenses - Set Amount")
                                print("Set the amount you've spent (number only, no commas)\n\nAmount: ")
                                try:
                                    amount_input = int(input())
                                    errmsg = errmsg.replace("|amount|", "")
                                    return amount_input
                                except ValueError:
                                    system("clear||cls")
                                    print("You must enter an integer.")
                        system("clear||cls")
                        amount = getAmount()
                    case "6":
                        system("clear||cls")
                        if(date == "null" or category == "null" or currency_symbol == "null" or amount == "null"):
                            errmsg = ""
                            errmsg += "|date| " if date == "null" else ""
                            errmsg += "|category| " if category == "null" else ""
                            errmsg += "|currency symbol| " if currency_symbol == "null" else ""
                            errmsg += "|amount| " if amount == "null" else ""
                            errmsg += " must not be null."
                            continue
                        else:
                            db_initCheck = cursor.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='expenses'; """).fetchall()
                            if db_initCheck == []:
                                cursor.execute("""CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT NOT NULL, category TEXT NOT NULL, description TEXT, currency_symbol TEXT, amount INTEGER NOT NULL); """)
                                sqliteConnection.commit()
                            cursor.execute("INSERT INTO expenses (date, category, description, currency_symbol, amount) VALUES (?, ?, ?, ?, ?)", (str(date), category, description, currency_symbol, int(amount)))
                            sqliteConnection.commit()
                            return
                    case "7":
                        system("clear||cls")
                        return
                    case "8":
                        system("clear||cls")
                        print("\nGoodbye.\n")
                        cursor.close()
                        sqliteConnection.close()
                        exit(0)
                    case _:
                        continue


        def viewExpenses():
            db_initCheck = cursor.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='expenses'; """).fetchall()
            if db_initCheck == []:
                cursor.execute("""CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT NOT NULL, category TEXT NOT NULL, description TEXT, currency_symbol TEXT, amount INTEGER NOT NULL); """)
                sqliteConnection.commit()
            result = cursor.execute("SELECT * FROM expenses ORDER BY date ASC, currency_symbol ASC;").fetchall()
            system("clear||cls")
            if not result:
                print("No expenses recorded.\n")
                input("Press ENTER to return.")
                system("clear||cls")
                return
            groupExpenses = {}
            for row in result:
                _id, date, category, description, currency, amount = row
                groupExpenses.setdefault(currency, []).append(row)
            for currency, entries in groupExpenses.items():
                print(f"\n==============================")
                print(f"Currency: {currency}")
                print("==============================")
                print(f"{'Date':<12} {'Category':<18} {'Amount':>10}  {'Description'}")
                print("-" * 60)
                total = 0
                for (_id, date, category, description, currency, amount) in entries:
                    total += amount
                    print(f"{date:<12} {category:<18} {currency}{amount:>8}  {description or '-'}")
                print("-" * 60)
                print(f"{'Total':<31} {currency}{total:>8.2f}")
                print()
            input("\nPress ENTER to return to the main menu...")
            system("clear||cls")
            return


        def summaryReport():
            system("clear||cls")
            print("Generating summary report...\n")
            cursor.execute("""CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT NOT NULL, category TEXT NOT NULL, description TEXT, currency_symbol TEXT, amount INTEGER NOT NULL);""")
            sqliteConnection.commit()
            result = cursor.execute("""SELECT date, SUM(amount) as total, currency_symbol FROM expenses GROUP BY date, currency_symbol ORDER BY date ASC;""").fetchall()
            system("clear||cls")
            if not result:
                print("No expenses recorded.\n")
                input("Press ENTER to return...")
                system("clear||cls")
                return
            expenses_by_currency = {}
            for date, total, currency in result:
                expenses_by_currency.setdefault(currency, []).append((date, total))
            plt.figure(figsize=(10, 6))
            for currency, entries in expenses_by_currency.items():
                dates = [datetime.datetime.strptime(d, "%Y-%m-%d") for d, _ in entries]
                totals = [t for _, t in entries]
                plt.plot(dates, totals, marker='o', label=f"{currency}")
            plt.title("Expenses Over Time")
            plt.xlabel("Date")
            plt.ylabel("Total Amount")
            plt.xticks(rotation=45)
            plt.legend(title="Currency")
            plt.tight_layout()
            output_file = f"summary_report-{datetime.datetime.now()}.png"
            plt.savefig(output_file)
            plt.close()
            print(f"Summary report saved as '{output_file}'.\n")
            print("You can open it using:")
            print(f"  open {output_file}   # macOS")
            print(f"  xdg-open {output_file}   # Linux")
            print(f"  start {output_file}   # Windows\n")
            input("Press ENTER to return to the main menu...")
            system("clear||cls")


        def editEntries():
            system("clear||cls")
            db_initCheck = cursor.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='expenses'; """).fetchall()
            if db_initCheck == []:
                cursor.execute("""CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY AUTOINCREMENT, date TEXT NOT NULL, category TEXT NOT NULL, description TEXT, currency_symbol TEXT, amount INTEGER NOT NULL); """)
                sqliteConnection.commit()
            result = cursor.execute("SELECT * FROM expenses ORDER BY date ASC, currency_symbol ASC;").fetchall()
            system("clear||cls")
            if not result:
                print("No expenses recorded.\n")
                input("Press ENTER to return.")
                system("clear||cls")
                return
            groupExpenses = {}
            for row in result:
                _id, date, category, description, currency, amount = row
                groupExpenses.setdefault(currency, []).append(row)

            cursor.execute("SELECT MAX(id) FROM expenses;")
            top_id = int(cursor.fetchone()[0])
            while True:
                system("clear||cls")
                for currency, entries in groupExpenses.items():
                    print(f"\n==============================")
                    print(f"Currency: {currency}")
                    print("==============================")
                    print(f"{'ID':<4} {'Date':<12} {'Category':<18} {'Amount':>10}  {'Description'}")
                    print("-" * 60)
                    total = 0
                    for (_id, date, category, description, currency, amount) in entries:
                        total += amount
                        print(f"{_id:<} {date:<12} {category:<18} {currency}{amount:>8}  {description or '-'}")
                    print("-" * 60)
                    print(f"{'Total':<31} {currency}{total:>8.2f}")
                    print()
                print("\n\nWhich entry would you like to edit? (id)\n\n")
                try:
                    entry_input = int(input())
                except ValueError:
                    print(f"Please enter a valid integer")
                    continue
                if entry_input < 0 or entry_input > top_id:
                    print(f"Please enter an integer between 0 and {top_id}")
                    continue
                else:
                    cursor.execute("SELECT * FROM expenses WHERE id = ?", (entry_input,))
                    result = cursor.fetchone()
                    if result is None:
                        system("clear||cls")
                        print(f"{entry_input} does not exist.")
                        continue
                    else:
                        system("clear||cls")
                        print(f"You have selected entry {result[0]}")
                        print(f"1. Date: {result[1]}\n2. Category: {result[2]}\n3. Description: {result[3]}\n4. Currency: {result[4]}\n5. Amount: {result[5]}")
                        print(f"\n\nWhat would you like to edit? (6 to exit)\n\n")
                        edit_input = input()
                        match edit_input:
                            case "1":
                                def getDate():
                                    while True:
                                        try:
                                            date_entry = input("Enter a date in YYYY-MM-DD format: ")
                                            year, month, day = map(int, date_entry.split('-'))
                                            date_input = datetime.date(year, month, day)
                                            return date_input
                                        except ValueError:
                                            system("clear||cls")
                                            print("Incorrect Date Format (Enter 0 to go back)")
                                            print(f"Edit Date\nCurrently Set: {result[1]}")
                                            if date_entry == "0":
                                                return result[1]
                                system("clear||cls")
                                print(f"Edit Date\nCurrently Set: {result[1]}")
                                print("\n\nEnter a new date (yyyy-mm-dd):\n")
                                new_date = getDate()
                                cursor.execute("UPDATE expenses SET date = ? WHERE id = ?", (str(new_date), result[0]))
                                sqliteConnection.commit()
                                print(f"{result[0]} has been updated. [{result[1]} -> {new_date}]")
                                break
                            case "2":
                                system("clear||cls")
                                print(f"Edit Category\nCurrently Set: {result[2]}")
                                print("Select a Category\n\n1. Food & Groceries\n2. Transport\n3. Entertainment\n4. Utilities\n5. Shopping\n6. Health\n7. Subscriptions\n8. Other\n\n")
                                category_selection = input()
                                category = result[2]
                                match category_selection:
                                    case "1":
                                        category = "Food & Groceries"
                                    case "2":
                                        category = "Transport"
                                    case "3":
                                        category = "Entertainment"
                                    case "4":
                                        category = 'Utilities'
                                    case "5":
                                        category = "Shopping"
                                    case "6":
                                        category = "Health"
                                    case "7":
                                        category = "Subscriptions"
                                    case "8":
                                        category = "Other"
                                    case _:
                                        continue
                                cursor.execute("UPDATE expenses SET category = ? WHERE id = ?", (category, result[0]))
                                sqliteConnection.commit()
                                print(f"\n\n{result[0]} has been updated. [{result[2]} -> {category}]")
                                break  
                            case "3":
                                system("clear||cls")
                                print(f"Set a description for your expense\n\nCurrent Description: {result[3]}\n\nEnter your description: ")
                                description = input()
                                if description == "":
                                    description = result[3]
                                cursor.execute("UPDATE expenses SET description = ? WHERE id = ?", (description, result[0]))
                                sqliteConnection.commit()
                                print(f"\n\n{result[0]} has been updated. [{result[3]} -> {description}]")
                                break
                            case "4":
                                system("clear||cls")
                                def getCurrencySymbol():
                                    print("Set the currency you're using (e.g $, £, ¥)\n\nSymbol: ")
                                    currency_input = input()
                                    return currency_input
                                system("clear||cls")
                                currency_symbol = getCurrencySymbol()
                                while len(currency_symbol) > 1:
                                    system("clear||cls")
                                    print("Please only enter 1 character.")
                                    currency_symbol = getCurrencySymbol()
                                cursor.execute("UPDATE expenses SET currency_symbol = ? WHERE id = ?", (currency_symbol, result[0]))
                                sqliteConnection.commit()
                                print(f"\n\n{result[0]} has been updated. [{result[4]} -> {currency_symbol}]")
                                break
                            case "5":
                                system("clear||cls")
                                def getAmount():
                                    while True:
                                        print("Set the amount you've spent (number only, no commas)\n\nAmount: ")
                                        try:
                                            amount_input = int(input())
                                            return amount_input
                                        except ValueError:
                                            system("clear||cls")
                                            print("You must enter an integer.")
                                system("clear||cls")
                                amount = getAmount()
                                cursor.execute("UPDATE expenses SET amount = ? WHERE id = ?", (amount, result[0]))
                                sqliteConnection.commit()
                                print(f"\n\n{result[0]} has been updated. [{result[5]} -> {amount}]")
                                break
                            case "6":
                                system("clear||cls")
                                return
                            case _:
                                break


        def main():
            system("clear||cls")
            while True:
                print("Expense Tracker By 0x0-V (Daniel Thomas)")
                print("\n\n1. Add Expense\n2. View expenses\n3. Summary Report\n4. Edit entries\n5. Exit\n\n")
                user_option = input()
                match user_option:
                    case "1":
                        system("clear||cls")
                        addExpense()
                        continue
                    case "2":
                        system("clear||cls")
                        viewExpenses()
                        continue
                    case "3":
                        system("clear||cls")
                        summaryReport()
                        continue
                    case "4":
                        system("clear||cls")
                        editEntries()
                        continue
                    case "5":
                        system("clear||cls")
                        cursor.close()
                        sqliteConnection.close()
                        print("Goodbye.")
                        break   
                    case _:
                        system("clear||cls")
                        print("Invalid Option.\n")
                        continue



        if __name__ == "__main__":
            main()


except KeyboardInterrupt:
    system("clear||cls")
    cursor.close()
    sqliteConnection.close()
    print("\nGoodbye.\n")

