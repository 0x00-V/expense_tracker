import os
from os import system
import os.path
import datetime
import sqlite3


try:
        try:
            sqliteConnection = sqlite3.connect('expenses.db')
            cursor = sqliteConnection.cursor()
        except sqlite3.Error as error:
            print('Error occured -', error)
            exit(1)



        def addExpense():
            #print("TBI")
            #query = 'SELECT sqlite_version();'
            #cursor.execute(query)
            #result = cursor.fetchall()
            #print('SQLite Version is {}'.format(result[0][0]))
            #exit(0)
            system("clear||cls")
            date = "null"
            category = "null"
            description = "null"
            currency_symbol = "null"
            amount = "null"

            while True:
                system("clear||cls")
                print("Expense Tracker - Add Expenses")
                print(f"\nDate: {date}\nCategory: {category}\nDescription: {description}\nCurrency: {currency_symbol}\nAmount: {amount}")
                print("\n\n1. Set Date\n2. Set Category\n3. Set Description\n4. Set Currency\n5. Set Amount\n\n6. Add Expenses\n7. Back\n8. Exit\n\n")
                user_option = input()
                system("clear||cls")

                match user_option:
                    case "1":
                        def getDate(): 
                            while True:
                                try:
                                    print("Expense Tracker - Add Expenses - Set Date")
                                    date_entry = input("Enter a date in YYYY-MM-DD format: ")
                                    year, month, day = map(int, date_entry.split('-'))
                                    date_input = datetime.date(year, month, day)
                                    return date_input
                                except:
                                    system("clear||cls")
                                    print("Incorrect Date Format") 
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
                                category = "null"
                    case "3":
                        system("clear||cls")
                        print("Expense Tracker - Add Expenses - Set Description")
                        print(f"Set a description for your expense\n\nCurrent Description: {description}\n\nEnter your description: ")
                        description = input()
                        system("clear||cls")
                    case "4":
                            def getCurrencySymbol():
                                print("Expense Tracker - Add Expenses - Set Currency")
                                print("Set the currency you're using (e.g $, £, ¥)\n\nSymbol: ")
                                currency_input = input()
                                return currency_input
                            system("clear||cls")
                            currency_symbol = getCurrencySymbol()
                            while len(currency_symbol) > 1:
                                system("clear||cls")
                                print("Please only enter 1 character.")
                                currency_symbol = getCurrencySymbol()
                    case "5":
                        def getAmount():
                            while True:
                                print("Expense Tracker - Add Expenses - Set Amount")
                                print("Set the amount you've spent (number only, no commas)\n\nAmount: ")
                                try:
                                    amount_input = int(input())
                                    return amount_input
                                except ValueError:
                                    system("clear||cls")
                                    print("You must enter an integer.")
                        system("clear||cls")
                        amount = getAmount()
                    case "6":
                        system("clear||cls")
                        print("To Be Implemented")
                    case "7":
                        system("clear||cls")
                        main()
                    case "8":
                        system("clear||cls")
                        print("\nGoodbye.\n")
                        exit(0)
                    case _:
                        continue



        def viewExpenses():
            print("TBI")
        def summaryReport():
            print("TBI")

        def main():
            system("clear||cls")
            while True:
                print("Expense Tracker By 0x0-V (Daniel Thomas)")
                print("\n\n1. Add Expense\n2. View expenses\n3. Summary Report\n4. Exit\n\n")
                user_option = input()
                match user_option:
                    case "1":
                        system("clear||cls")
                        addExpense()
                        continue
                    case "2":
                        system("clear||cls")
                        addExpense()
                        continue
                    case "3":
                        system("clear||cls")
                        addExpense()
                        continue
                    case "4":
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
    print("\nGoodbye.\n")

