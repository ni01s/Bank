from tkinter import *
from tkinter import messagebox, simpledialog

# Global user database
users = {}
current_user = {}

def create_account():
    name = name_entry.get()
    age = age_entry.get()
    salary = salary_entry.get()
    pin = pin_entry.get()

    if not name or not age or not salary or not pin:
        messagebox.showerror("Error", "All fields are required!")
        return
    if not age.isdigit() or not salary.isdigit():
        messagebox.showerror("Error", "Age and Salary must be numbers!")
        return
    if not pin.isdigit() or len(pin) != 4:
        messagebox.showerror("Error", "PIN must be a 4-digit number!")
        return

    users[pin] = {"name": name, "age": age, "salary": salary, "balance": 0, "transactions": []}
    messagebox.showinfo("Success", "Account created successfully!")

    # Clear fields
    name_entry.delete(0, END)
    age_entry.delete(0, END)
    salary_entry.delete(0, END)
    pin_entry.delete(0, END)

def login():
    global current_user
    name = login_name_entry.get()
    pin = login_pin_entry.get()

    if pin in users and users[pin]["name"] == name:
        current_user = users[pin]
        show_user_frame()
    else:
        messagebox.showerror("Error", "Invalid name or PIN!")

def show_user_frame():
    login_frame.pack_forget()
    create_account_frame.pack_forget()
    user_frame.pack()
    update_user_labels()

def update_user_labels():
    name_label_val.config(text=current_user["name"])
    age_label_val.config(text=current_user["age"])
    salary_label_val.config(text=current_user["salary"])
    balance_label_val.config(text=current_user["balance"])

def deposit():
    amount = simpledialog.askinteger("Deposit", "Enter amount to deposit:")
    if amount and amount > 0:
        current_user["balance"] += amount
        current_user["transactions"].append(f"Deposited: +{amount}")
        update_user_labels()

def withdraw():
    amount = simpledialog.askinteger("Withdraw", "Enter amount to withdraw:")
    if amount and 0 < amount <= current_user["balance"]:
        current_user["balance"] -= amount
        current_user["transactions"].append(f"Withdrawn: -{amount}")
        update_user_labels()
    else:
        messagebox.showerror("Error", "Invalid or insufficient balance.")

def view_transactions():
    top = Toplevel()
    top.title("Transactions")
    listbox = Listbox(top, width=50)
    listbox.pack(padx=10, pady=10)
    for t in current_user["transactions"]:
        listbox.insert(END, t)

def logout():
    user_frame.pack_forget()
    create_account_frame.pack()
    login_frame.pack()

root = Tk()
root.title("Bank Management System")
root.geometry("400x400")

# ==== Create Account Frame ====
create_account_frame = Frame(root)
create_account_frame.pack(pady=10)

Label(create_account_frame, text="Name:").grid(row=0, column=0)
name_entry = Entry(create_account_frame)
name_entry.grid(row=0, column=1)

Label(create_account_frame, text="Age:").grid(row=1, column=0)
age_entry = Entry(create_account_frame)
age_entry.grid(row=1, column=1)

Label(create_account_frame, text="Salary:").grid(row=2, column=0)
salary_entry = Entry(create_account_frame)
salary_entry.grid(row=2, column=1)

Label(create_account_frame, text="PIN:").grid(row=3, column=0)
pin_entry = Entry(create_account_frame, show="*")
pin_entry.grid(row=3, column=1)

Button(create_account_frame, text="Create Account", command=create_account).grid(row=4, column=1, pady=10)

# ==== Login Frame ====
login_frame = Frame(root)
login_frame.pack(pady=10)

Label(login_frame, text="Name:").grid(row=0, column=0)
login_name_entry = Entry(login_frame)
login_name_entry.grid(row=0, column=1)

Label(login_frame, text="PIN:").grid(row=1, column=0)
login_pin_entry = Entry(login_frame, show="*")
login_pin_entry.grid(row=1, column=1)

Button(login_frame, text="Login", command=login).grid(row=2, column=1, pady=10)

# ==== User Frame ====
user_frame = Frame(root)

Label(user_frame, text="Welcome!").grid(row=0, columnspan=2)
Label(user_frame, text="Name:").grid(row=1, column=0)
name_label_val = Label(user_frame, text="")
name_label_val.grid(row=1, column=1)

Label(user_frame, text="Age:").grid(row=2, column=0)
age_label_val = Label(user_frame, text="")
age_label_val.grid(row=2, column=1)

Label(user_frame, text="Salary:").grid(row=3, column=0)
salary_label_val = Label(user_frame, text="")
salary_label_val.grid(row=3, column=1)

Label(user_frame, text="Balance:").grid(row=4, column=0)
balance_label_val = Label(user_frame, text="")
balance_label_val.grid(row=4, column=1)

Button(user_frame, text="Deposit", command=deposit).grid(row=5, column=0, pady=5)
Button(user_frame, text="Withdraw", command=withdraw).grid(row=5, column=1)
Button(user_frame, text="Transactions", command=view_transactions).grid(row=6, column=0, columnspan=2)
Button(user_frame, text="Logout", command=logout).grid(row=7, column=0, columnspan=2)

root.mainloop()
