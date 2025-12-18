from tkinter import *
from tkinter import messagebox, simpledialog

# ---------------- DATA ----------------
users = {}
current_user = None

# ---------------- FUNCTIONS ----------------
def clear_entries(*entries):
    for e in entries:
        e.delete(0, END)

def create_account():
    name = name_e.get()
    age = age_e.get()
    salary = salary_e.get()
    pin = pin_e.get()

    if not all([name, age, salary, pin]):
        messagebox.showerror("Error", "All fields required")
        return
    if not age.isdigit() or not salary.isdigit():
        messagebox.showerror("Error", "Age & Salary must be numbers")
        return
    if not pin.isdigit() or len(pin) != 4:
        messagebox.showerror("Error", "PIN must be 4 digits")
        return

    users[pin] = {
        "name": name,
        "age": age,
        "salary": salary,
        "balance": 0,
        "transactions": []
    }

    messagebox.showinfo("Success", "Account Created")
    clear_entries(name_e, age_e, salary_e, pin_e)

def login():
    global current_user
    pin = login_pin_e.get()
    name = login_name_e.get()

    if pin in users and users[pin]["name"] == name:
        current_user = users[pin]
        show_user()
    else:
        messagebox.showerror("Error", "Invalid Login")

def show_user():
    create_frame.pack_forget()
    login_frame.pack_forget()
    user_frame.pack()
    update_labels()

def update_labels():
    name_val.config(text=current_user["name"])
    age_val.config(text=current_user["age"])
    salary_val.config(text=current_user["salary"])
    balance_val.config(text=current_user["balance"])

def deposit():
    amt = simpledialog.askinteger("Deposit", "Enter amount")
    if amt and amt > 0:
        current_user["balance"] += amt
        current_user["transactions"].append(f"+{amt} Deposited")
        update_labels()

def withdraw():
    amt = simpledialog.askinteger("Withdraw", "Enter amount")
    if amt and 0 < amt <= current_user["balance"]:
        current_user["balance"] -= amt
        current_user["transactions"].append(f"-{amt} Withdrawn")
        update_labels()
    else:
        messagebox.showerror("Error", "Insufficient Balance")

def show_transactions():
    top = Toplevel()
    top.title("Transactions")
    lb = Listbox(top, width=40)
    lb.pack(padx=10, pady=10)
    for t in current_user["transactions"]:
        lb.insert(END, t)

def logout():
    user_frame.pack_forget()
    create_frame.pack()
    login_frame.pack()

# ---------------- UI ----------------
root = Tk()
root.title("Bank System")
root.geometry("350x400")

# ---- Create Account ----
create_frame = Frame(root)
create_frame.pack(pady=10)

Label(create_frame, text="Create Account", font=("Arial", 12)).grid(row=0, columnspan=2)

Label(create_frame, text="Name").grid(row=1, column=0)
name_e = Entry(create_frame)
name_e.grid(row=1, column=1)

Label(create_frame, text="Age").grid(row=2, column=0)
age_e = Entry(create_frame)
age_e.grid(row=2, column=1)

Label(create_frame, text="Salary").grid(row=3, column=0)
salary_e = Entry(create_frame)
salary_e.grid(row=3, column=1)

Label(create_frame, text="PIN").grid(row=4, column=0)
pin_e = Entry(create_frame, show="*")
pin_e.grid(row=4, column=1)

Button(create_frame, text="Create", command=create_account).grid(row=5, columnspan=2, pady=5)

# ---- Login ----
login_frame = Frame(root)
login_frame.pack(pady=10)

Label(login_frame, text="Login", font=("Arial", 12)).grid(row=0, columnspan=2)

Label(login_frame, text="Name").grid(row=1, column=0)
login_name_e = Entry(login_frame)
login_name_e.grid(row=1, column=1)

Label(login_frame, text="PIN").grid(row=2, column=0)
login_pin_e = Entry(login_frame, show="*")
login_pin_e.grid(row=2, column=1)

Button(login_frame, text="Login", command=login).grid(row=3, columnspan=2, pady=5)

# ---- User Panel ----
user_frame = Frame(root)

Label(user_frame, text="Account Details", font=("Arial", 12)).grid(row=0, columnspan=2)

Label(user_frame, text="Name").grid(row=1, column=0)
name_val = Label(user_frame)
name_val.grid(row=1, column=1)

Label(user_frame, text="Age").grid(row=2, column=0)
age_val = Label(user_frame)
age_val.grid(row=2, column=1)

Label(user_frame, text="Salary").grid(row=3, column=0)
salary_val = Label(user_frame)
salary_val.grid(row=3, column=1)

Label(user_frame, text="Balance").grid(row=4, column=0)
balance_val = Label(user_frame)
balance_val.grid(row=4, column=1)

Button(user_frame, text="Deposit", command=deposit).grid(row=5, column=0)
Button(user_frame, text="Withdraw", command=withdraw).grid(row=5, column=1)
Button(user_frame, text="Transactions", command=show_transactions).grid(row=6, columnspan=2)
Button(user_frame, text="Logout", command=logout).grid(row=7, columnspan=2)

root.mainloop()

