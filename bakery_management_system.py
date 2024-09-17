# Bakery Management System

import pandas as pd
import datetime
import os


def add_item(df):
    ch = input("Press 1 to continue or Press 0 to go back to main menu : ")

    if ch.isnumeric():
        if int(ch)==1:

            # This while part is added because if user give invalid data for name,order_name and quantity then it will ask again for details until user give correct input
            while True:
                name = input("Enter customer name : ")
                order_dt = datetime.datetime.now()
                order_name = input("Enter your order name : ")
                quantity = input('Enter the qunatity of order customer want : ')
                # amount = input("Enter the amount of order : ")
                
                if name.isalpha() and order_name.isalpha() and quantity.isnumeric() :#and amount.isnumeric():
                    order_id = len(df)+1
                    data = {
                        'Order_id' : order_id,
                        'Name' : name,
                        'Item Name' : order_name,
                        'Quantity' : int(quantity),
                        # 'Amount' : float(amount),
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
                                    if order_id in list(df['Order_id']):
                                        print(df[df['Order_id']==order_id])
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
                            # Order_id is set as index so that updation can be done based on order_id
                            df.set_index('Order_id',inplace=True)
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
                                        print()
                                        print(f"Order id {index} doesn't exists")
                                        print("-------------------------------------------------------")
                                        print()

                                    else:
                                        print()
                                        print(f"{col} column doesn't exists")
                                        print("----------------------------------------------")
                                        print()
                                    
                                    break

                                else:
                                    print()
                                    print("Enter the valid data for each input.")
                                    print("---------------------------------------")
                                    print()

                            # Once order is updated based on order_id as index then index is set back to default inedx of dataframe
                            df.reset_index(inplace=True)

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


def invoice(df, menu_df):

    # If dataframe (df) is not empty then generate the invoice otherwise no invoice will be generated
    if not df.empty and not menu_df.empty:
        invoice_df = pd.merge(df , menu_df , on="Item Name")

        # Total Price = Quantity * Price
        invoice_df["Total Price"] = invoice_df["Quantity"] * invoice_df["Price (INR)"]

        # Grand Total = Sum of all Total Price
        grand_total = invoice_df["Total Price"].sum()

        # Creating a new row for grand total cell
        grand_total_row = pd.DataFrame([['','','','','','Grand Total',grand_total]] , columns=['Order_id','Name','Item Name','Quantity','Order_date','Price (INR)','Total Price'])
        
        # To add grand_total as a row in dataframe in final invoice
        final_invoice_df = pd.concat([invoice_df , grand_total_row] , ignore_index=True)

        # Move order_date column to the rightest side in dataframe
        final_invoice_df = final_invoice_df[['Order_id','Name','Item Name','Quantity','Price (INR)','Total Price','Order_date']]

        # Saving dataframe into excel
        final_invoice_df.to_excel('Customer_invoice.xlsx', index=False)
        print("Invoice generated and stored in excel format successfully ✅")
        print()

        # Returning a dataframe without index column i.e which starst from 0
        return print(final_invoice_df.to_string(index=False))
    
    else:
        print("No items added yet🤔..why you want to pay bill without buying anything😅")


# For using pdf format
from fpdf import FPDF

def download_invoice(df , menu_df):

    if not df.empty and not menu_df.empty:
        invoice_df = pd.merge(df , menu_df , on="Item Name")

        # Total Price = Quantity * Price
        invoice_df["Total Price"] = invoice_df["Quantity"] * invoice_df["Price (INR)"]

        # Grand Total = Sum of all Total Price
        grand_total = invoice_df["Total Price"].sum()


        # Step to Generate PDF using FPDF
        class PDF(FPDF):
            def header(self):
                # Add Invoice Header
                self.set_font('Arial', 'B', 12)
                self.cell(0, 10, 'Bakery Shop Invoice', 0, 1, 'C')

            def footer(self):
                # Add Footer (Page Number)
                self.set_y(-15)
                self.set_font('Arial', 'I', 8)
                self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

            def invoice_body(self, invoice_df, grand_total):
                # Add Invoice Body
                self.set_font('Arial', '', 12)
                self.cell(0, 10, 'Customer Order:', 0, 1)

                # Invoice table header
                self.cell(50, 10, 'Item Name', 1)
                self.cell(30, 10, 'Quantity', 1)
                self.cell(40, 10, 'Price (INR)', 1)
                self.cell(50, 10, 'Total Price', 1)
                self.ln()

                # Invoice table body
                for index, row in invoice_df.iterrows():
                    self.cell(50, 10, row['Item Name'], 1)
                    self.cell(30, 10, str(row['Quantity']), 1)
                    self.cell(40, 10, str(row['Price (INR)']), 1)
                    self.cell(50, 10, str(row['Total Price']), 1)
                    self.ln()

                # Grand total
                self.cell(50, 10, '', 0)
                self.cell(30, 10, '', 0)
                self.cell(40, 10, 'Grand Total', 1)
                self.cell(50, 10, str(grand_total), 1)
                self.ln()

        # Create PDF instance and generate the invoice
        pdf = PDF()
        pdf.add_page()
        pdf.invoice_body(invoice_df, grand_total)

        # Step 7: Save the PDF
        pdf_output_path = "Customer_invoice.pdf"
        pdf.output(pdf_output_path)

        print(f'Invoice downloaded as pdf format successfully ✅')
    
    else:
        print("You haven't buy anything yet🤔...then why to download the bill😅")



def base(df):

    while True:
        choice = input('''Welcome to Bakery Management System🍔🍟🎂 \
                           \n1. Add an item \
                           \n2. Update an item \
                           \n3. Display order details \
                           \n4. Export data to excel sheet \
                           \n5. Load the existing data \
                           \n6. Menu \
                           \n7. Generate Invoice \
                           \n8. Download Invoice \
                           \n9. Clear the screen \
                           \n10. Exit \
                           \nSelect the option number : ''')
        
        # This part is to check whether choice is integer or not
        if choice.isnumeric():
            choice = int(choice)
            if choice==1:
                os.system('cls')
                new_df = add_item(df)

                # 'ignore_index=True' parameter makes sure that the appended row gets an appropriate new index.
                df = df._append(new_df, ignore_index=True)
                
                # # Sets custom column as index
                # df.set_index('Order_id',inplace=True)

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
                    print("---------------------------------------------------------")
                    print()
                else:
                    os.system('cls')
                    save_data(df)

            elif choice==5:
                os.system('cls')
                df = load_data()

            elif choice==6:
                os.system('cls')

                # You can't directly remove the index from the DataFrame when reading it, but you can exclude it while printing like this :

                # Reading the Excel file (index will still be there in the DataFrame i.e 1st column will also be printed starting from 0)
                menu_df = pd.read_excel('Bakery_Menu.xlsx')

                # Printing the DataFrame without the index
                print(menu_df.to_string(index=False))
                print("---------------------------------------------------------------------------------")
                print()

            elif choice==7:
                os.system('cls')

                menu_df = pd.read_excel('Bakery_Menu.xlsx')
                invoice(df , menu_df)
                print("--------------------------------------------------------------------------------------------")
                print()

            elif choice==8:
                os.system('cls')
                menu_df = pd.read_excel('Bakery_Menu.xlsx')
                download_invoice(df , menu_df)
                print("---------------------------------------------------------------------")
                print()

            elif choice==9:
                os.system('cls')

            elif choice==10:
                os.system('cls')
                print("Happy Earning😉")
                exit()
            else:
                print()
                print("Select from above six options only")
                print("--------------------------------------------")
                print()

        else:
            print()
            print("Select from above options only.")
            print("--------------------------------------")
            print()

df = pd.DataFrame()
base(df)
