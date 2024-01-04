import tkinter as tk
from tkinter import messagebox
import mysql.connector

#connect to MySQL database
mydb= mysql.connector.connect(
   host= "localhost",
   user= "root",
   password= "",
   database= "crochet_purchase"
)

#cursor object
mycursor = mydb.cursor()

# calculation and database saving
def collect_data():
    buyername = name_entry.get()
    buyeradress = adress_entry.get()
    buyernumber = phone_entry.get()
    producttype = product_type.get()  # Fixed variable name
    total = total_entry.get()

    print("Name:", buyername, "Address:", buyeradress, "Phone Number", buyernumber)
    print("Select Your Product", producttype, "Total:", total)
    print("-------------------------------------------------")

    # Inserting data into a table
    sql="INSERT INTO crochet_purchase (NAME,ADDRESS,NO_PHONE,PRODUCT_TYPE,TOTAL) VALUES (%s,%s,%s,%s,%s)"
    val = (buyername,buyeradress,buyernumber,producttype,total)

    try:
        mycursor.execute(sql, val)
        mydb.commit()
        print("Data inserted successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        mydb.rollback()

    jumlah = int(total_entry.get())

    # prices of product
    prices = {
        "Product A": 6,
        "Product B": 35,
        "Product C": 10,
        "Product D": 30,
    }

    # calculation
    total_prices = prices[producttype] * jumlah  # Fixed variable name

    # output
    output_label.config(text=f"Total Price: RM{total_prices}")
    output_label.pack(pady=5)


# Main window
root = tk.Tk()
root.title("CROCHET BY WANIE")
root.geometry('500x600')
root.configure(bg='pink')

# Page title
label = tk.Label(root, text='CROCHET PURCHASE', font=("Input Mono", 30, "bold"), fg='#FF1493', bg='pink')
label.pack(padx=20, pady=10)

frame = tk.Frame(root, bg='pink')
frame.pack()

info = tk.LabelFrame(frame, text="", bg='pink')
info.grid(row=0, column=1, sticky="News", padx=1, pady=1)

# customer information
name_label = tk.Label(info, text="Name:", bg='#FF83FA', font=("Times New Roman", 15, "bold"))
name_label.pack()
name_entry = tk.Entry(info)
name_entry.pack(pady=15)

adress_label = tk.Label(info, text="Address:", bg='#FF83FA', font=("Times New Roman", 15, "bold"))
adress_label.pack()
adress_entry = tk.Entry(info)
adress_entry.pack(pady=15)

phone_label = tk.Label(info, text="Phone Number:", bg='#FF83FA', font=("Times New Roman", 15, "bold"))
phone_label.pack()
phone_entry = tk.Entry(info)
phone_entry.pack(pady=15)

price_frame = tk.LabelFrame(frame, text="", bg='pink')
price_frame.grid(row=0, column=0, sticky="News", padx=1, pady=1)

# Price List
price_text = tk.Text(price_frame, height=1, width=17, font=("bold", 20), fg='purple', bg='#FF83FA')
price_text.pack(pady=5, padx=10)
# Pricebox
price_text.insert(tk.END, "PRODUCT & PRICE")
price_text.config(state="disabled")

# Product List
productA_text = tk.Text(price_frame, height=2, width=25, font=(10), fg='purple', bg='#EE3A8C')
productA_text.pack(pady=5)
# ProductA box
productA_text.insert(tk.END, "Product A: Keychain \nPrice: RM6")
productA_text.config(state="disabled")

# Product List
productB_text = tk.Text(price_frame, height=2, width=25, font=(10), fg='purple', bg='#FF82AB')
productB_text.pack(pady=5)
# ProductB Box
productB_text.insert(tk.END, "Product B: Plushie \nPrice: RM35")
productB_text.config(state="disabled")

# Product List
productC_text = tk.Text(price_frame, height=2, width=25, font=(10), fg='purple', bg='#EE3A8C')
productC_text.pack(pady=5)
# ProductC Box
productC_text.insert(tk.END, "Product C: Flower \nPrice: RM10")
productC_text.config(state="disabled")

# Product List
productD_text = tk.Text(price_frame, height=2, width=25, font=(10), fg='purple', bg='#FF82AB')
productD_text.pack(pady=5)
# ProductD Box
productD_text.insert(tk.END, "Product D: Beanie \nPrice: RM30")
productD_text.config(state="disabled")

product = tk.LabelFrame(frame, bg='pink')
product.grid(row=1, column=0, sticky="News", padx=1, pady=1)

# product type dropdown
ttl_label = tk.Label(product, text="Choose Your Product", bg='#FF83FA', font=("Times New Roman", 15, "bold"))
ttl_label.pack(padx=5)

product_type = tk.StringVar(root)
product_type.set("Select Your Product")
product_dropdown = tk.OptionMenu(product, product_type, "Product A", "Product B", "Product C", "Product D")
product_dropdown.pack(pady=10)

# total entry
total_label = tk.Label(product, text="Total:", bg='#FF83FA', font=("Times New Roman", 15, "bold"))
total_label.pack()
total_entry = tk.Entry(product)
total_entry.pack(pady=5)

total = tk.LabelFrame(frame, text="", bg='pink')
total.grid(row=1, column=1, sticky="News", padx=1, pady=1)

# Save Button
save_button = tk.Button(total, text="Calculate", font=("Times New Roman", 15, "bold"), bg='#FF6A6A', command=collect_data)
save_button.pack(pady=10)

# output label & result
label = tk.Label(total, text='Prices Product', bg='#FF83FA', font=("Times New Roman", 15, "bold"))
label.pack(ipadx=10, ipady=10)

output_label = tk.Label(total, text="")
output_label.pack()

# Accept terms
terms_frame = tk.LabelFrame(frame, text="Terms and Conditions.", font=("Times New Roman", 15, "bold"), bg='pink')
terms_frame.grid(column=0, sticky="news")

# accept_var = tk.StringVar(value="not accepted")
# terms_check= tk.Checkbutton(terms_frame, text= "I accept the terms and conditions.",variable=accept_var, onvalue="acepted", offvalue="not accepted",bg= 'pink')
# terms_check.grid(row=2, column=0)

root.mainloop()

# Close the cursor and the connection when the application is closed
mycursor.close()
mydb.close()