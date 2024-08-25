# Bakery Management System

import pandas as pd
import datetime
import os


def add_item():
    ch = input("Press 1 to continue or Press 0 to go back to main menu : ")

    if ch.isnumeric():
        if int(ch)==1:

            # This while part is added because if user give invalid data for name,order_name and quantity then it will ask again for details until user give correct input
            while True:
                name = input("Enter customer name : ")
                order_dt = datetime.datetime.now()
                order_name = input("Enter your order name : ")
                quantity = input('Enter the qunatity of order customer want : ')
                amount = input("Enter the amount of order : ")
                
                if name.isalpha() and order_name.isalpha() and quantity.isnumeric() and amount.isnumeric():
                    data = {
                        'Name' : name,
                        'Order_name' : order_name,
                        'Quantity' : int(quantity),
                        'Amount' : float(amount),
                        'Order_date' : order_dt
                    }

                    # once data is valid come out of loop
                    break

                else:
                    print()
                    print("Enter valid data for each input.")
                    print("----------------------------------")
                    print()

            print("1 Item added ✅")
            print("----------------------------------")
            return data
        
        elif int(ch)==0:
            os.system('cls')
            base(df)
        
        else:
            # This part is for if ch is other than 0 or 1
            print()
            print("Select either 1 or 0")
            print("---------------------------------------")
            add_item()

    else:
        # This part is for ch is other than integer
        print("Select your choice from above two options")
        print("----------------------------------------")
        print()
        add_item()




def update(df):
    if df.empty:
        print("No item inserted yet😕\nAdd item first")
    else:
        ch = input("Press 1 to continue or Press 0 to go back to main menu : ")
        print()

        if ch.isnumeric():
            ch = int(ch)
            if ch==1:

                # This while shows options until user won't exit from the update menu
                while(True):
                    update_choice = input('''1. Press 1 to see the entire order details (so that you can't update wrong order 😅) \
                            \n2. Press 2 to see a particular order details \
                            \n3. Press 3 to update the required order (if you remembered the order_id 😎) \
                            \n4. Press 4 to exit the update menu \n \
                            \nSelect your choice from above option : ''')
                    
                    # This if part is for checking whether update_choice is integer or not
                    if update_choice.isnumeric():
                        update_choice = int(update_choice)
                        if update_choice==1:
                            display(df)
                            print()
                            print("------------------------------------------------")
                            print()

                        elif update_choice==2:
                            # This while loop runs until order_id is not valid
                            while True:
                                print()
                                order_id = input("Enter the order_id you want to see detail : ")
                                if order_id.isnumeric():
                                    order_id = int(order_id)
                                    if order_id in list(df.index):
                                        center_aligned_df = df.style.set_properties(**{'text-align': 'center'})
                                        print(center_aligned_df.iloc[[order_id]])
                                        print("---------------------------------------------------------------------------")
                                        print()
                                    else:
                                        print()
                                        print("Order id doesn't exist in the database")
                                        print("------------------------------------------------")
                                        print()
                                    break
                                else:
                                    print()
                                    print("Enter a valid order_id")
                                    print()

                            
                        elif update_choice==3:
                            print()

                            while True:
                                index = input("Enter the order id you want to update : ")
                                col = input("Enter the column you want to update : ")         
                                new_col_value = input("Enter the new value : ")

                                # This code is build for updating only quantity and amount column as of now and not able to handle name column because new_col_value accepts only inetger value as of now
                                # This part checks wheather each input is valid or not i.e index -> integer , col -> alphabets , new_col_value -> integer
                                if index.isnumeric() and col.isalpha() and new_col_value.isnumeric():

                                    index = int(index)

                                    if index in list(df.index) and col in list(df.columns):
                                        df.loc[index , col] = new_col_value
                                        print()
                                        print(f"{col} updated successfully ✅")
                                        print("--------------------------------------------------------")
                                        print()

                                    elif index not in list(df.index):
                                        print(f"Order id {index} doesn't exists")
                                        print("-------------------------------------------------------")
                                        print()

                                    else:
                                        print(f"{col} column doesn't exists")
                                        print("----------------------------------------------")
                                        print()
                                    
                                    break

                                else:
                                    print()
                                    print("Enter the valid data for each input.")
                                    print("---------------------------------------")
                                    print()
                        
                        elif update_choice==4:
                            print("-------------------------------------------------")
                            break

                        else:
                            print()
                            print("Select from above four options only")
                            print("------------------------------------------")
                            print()
                    
                    else:
                        # This part is for for update_choice is alphabets or alphanumeric input
                        print("Choose the valid options")
                        print()

            elif ch==0:
                os.system('cls')
                base(df)

            else:
                # This part is for if ch is other than 0 or 1
                print()
                print("Select either 1 or 0")
                print("----------------------------------------")
                update(df)

        else:
            # This part is for if ch is other than integer
            print("Select your choice from above two options")
            print("---------------------------------------------")
            print()
            update(df)



def display(df):
    if df.empty:
        print("Nothing to display yet..add item first")
    else:
        print(df)


def save_data(df):
    file_name = input("Name the file to save your data : ")
    path = f'{file_name}.xlsx'
    if os.path.exists(path):
        print(f"{path} file already exists in current directory")
        print()

        while True:
            override = input("Do you want to override the content of the file?\nPress Y to override or N to discard : ")
            
            if override.isalpha() and len(override)==1:
                if override.lower()=='y':
                    try:
                        # index=False means default index of dataframe is not stored in excel sheet
                        df.to_excel(f'{file_name}.xlsx', index=False)
                    except:
                        print()
                        print("An error occurred while exporting the data to file")
                        print("-----------------------------------------------------")
                        print()
                    else:
                        print()
                        print(f"Data exported to {file_name}.xlsx file succesfully ✅")
                        print("---------------------------------------------------")
                        print()
                elif override.lower()=='n':
                    print()
                    print("No data exported yet")
                    print("---------------------------------")
                
                else:
                    print()
                    print("Choose the input from Y or N\n")
                    continue

                break

            elif len(override)!=1:
                print("Choose the input from Y or N\n")

            else:
                print("Choose the input from Y or N\n")

    else:
        try:
            # index=False means default index of dataframe is not stored in excel sheet
            df.to_excel(f'{file_name}.xlsx', index=False)
        except:
            print("An error occurred while exporting the data to file")
            print("-----------------------------------------------------")
            print()
        else:
            print(f"Data exported to {file_name}.xlsx file succesfully ✅")
            print("---------------------------------------------------")
            print()



def load_data():
    load_file_name = input("Enter the previously saved filename to load : ")
    path = f'{load_file_name}.xlsx'

    if os.path.exists(path):
        try:
            df = pd.read_excel(f'{load_file_name}.xlsx')
        except:
            print(f"An error occurred while importing data from {load_file_name}")
            print("-----------------------------------------------------")
            print()
        else:
            print(f"Data imported from {load_file_name}.xlsx succesfully ✅")
            print("---------------------------------------------------")
            print()
            return df
    else:
        print()
        print("No such file exists in current directory")
        print("---------------------------------------------")
        print()



def base(df):

    while True:
        choice = input('''Welcome to Bakery Management System🍔🍟🎂 \
                           \n1. Add an item \
                           \n2. Update an item \
                           \n3. Display order details \
                           \n4. Export data to excel sheet \
                           \n5. Load the existing data \
                           \n6. Clear the screen \
                           \n7. Exit \
                           \nSelect the option number : ''')
        
        # This part is to check whether choice is integer or not
        if choice.isnumeric():
            choice = int(choice)
            if choice==1:
                os.system('cls')
                new_df = add_item()
                df = df._append(new_df, ignore_index=True)
                print()

            elif choice==2:
                os.system('cls')
                update(df)
                print()

            elif choice==3:
                os.system('cls')
                display(df)
                print()
                print("-------------------------------------------------------------------")
                print()

            elif choice==4:
                os.system('cls')
                if df.empty:
                    print("Buddy insert item first then export your data 😄")
                    print("-------------------------------------------------------")
                    print()
                else:
                    os.system('cls')
                    save_data(df)

            elif choice==5:
                os.system('cls')
                df = load_data()

            elif choice==6:
                os.system('cls')

            elif choice==7:
                os.system('cls')
                print("Happy Earning😉")
                exit()
            else:
                print()
                print("Select from above six options only")
                print("------------------------------------------")
                print()

        else:
            print()
            print("Select from above options only.")
            print("--------------------------------------")
            print()

df = pd.DataFrame()
base(df)
