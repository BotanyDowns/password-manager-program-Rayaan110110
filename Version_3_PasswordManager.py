from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext

# Creating an empty dictionary to store account name and password
passwords = {}

# Using 3 functions like adding passwords to account and asking to get password from dictionary
def add_password(account, password):
    passwords[account] = password
    
def get_password(account):
    return passwords.get(account, None)

def show_passwords():
    password_list = ""
    for account, password in passwords.items():
        password_list += f"{account}: {password}\n"
    if password_list:
        password_window = Toplevel(root)
        password_window.title("Saved Passwords")
        password_window.geometry("200x200")
        password_text = scrolledtext.ScrolledText(password_window, width=25, height=15)
        password_text.pack()
        password_text.insert(END, password_list)
        password_text.config(state=DISABLED)
    else:
        messagebox.showwarning(title="No passwords found", message="No passwords have been saved yet.")

def delete_password():
    account = account_entry.get()
    if account in passwords:
        del passwords[account]
        messagebox.showinfo(title="Password Deleted", message=f"Password for {account} has been deleted.")
        account_entry.delete(0, END)
    else:
        messagebox.showwarning(title="No password found", message=f"No password found for {account}.")        

# Creating GUI using Tkinter
root = Tk()
root.title("Password Manager")
root.configure(bg="#1a1a1a") # set background color to grey

# Creating frames for spacing
input_frame = Frame(root, bg="#1a1a1a")
input_frame.pack(padx=20, pady=20)

output_frame = Frame(root, bg="#1a1a1a")
output_frame.pack(padx=20, pady=20)

# Adding widgets to the input frame
# Creating the label for the Account Name
account_label = Label(input_frame, text="Account Name", bg="#1a1a1a", fg="white")
account_label.pack()

# Creating the entry box for the Account Name
account_entry = Entry(input_frame)
account_entry.pack()

# Creating the label for the Password
password_label = Label(input_frame, text="Password", bg="#1a1a1a", fg="white")
password_label.pack()

# Creating the entry box for the Password
password_entry = Entry(input_frame, show="*")
password_entry.pack()

# Creating the button to save the password
def save_password():
    account = account_entry.get()
    password = password_entry.get()
    if not account or not password:
        messagebox.showwarning(title="Missing Input", message="Please enter both account name and password.")
    else:
        add_password(account, password)
        account_entry.delete(0, END)
        password_entry.delete(0, END)    

save_button = Button(input_frame, text="Add Password", command=save_password, bg="#00bfff", fg="white")
save_button.pack(pady=10)

# Adding widgets to the output frame
# Creating the button to get the password
def get_password_callback():
    account = account_entry.get()
    password = get_password(account)
    if password:
        messagebox.showinfo(title="Password", message=f"Password for {account}: {password}")
    else:
        messagebox.showwarning(title="No password found", message=f"No password found for {account}")

get_password_button = Button(output_frame, text="Get Password", command=get_password_callback, bg="#00bfff", fg="white")
get_password_button.pack(side=TOP, padx=5, pady=10)

# Creating the button to update a password
def update_password_callback():
    account = account_entry.get()
    password = get_password(account)
    if password:
        update_window = Toplevel(root)
        update_window.title("Update Password")
        update_window.geometry("300x150")

        old_password_label = Label(update_window, text="Old Password", bg="#1a1a1a", fg="white")
        old_password_label.pack()

        old_password_entry = Entry(update_window, show="*")
        old_password_entry.pack()

        new_password_label = Label(update_window, text="New Password", bg="#1a1a1a", fg="white")
        new_password_label.pack()

        new_password_entry = Entry(update_window, show="*")
        new_password_entry.pack()

        def update_password():
            old_password = old_password_entry.get()
            new_password = new_password_entry.get()
            if old_password != password:
                messagebox.showwarning(title="Incorrect Password", message="Old password entered does not match saved password.")
            elif not new_password:
                messagebox.showwarning(title="Missing Input", message="Please enter a new password.")
            else:
                add_password(account, new_password)
                update_window.destroy()
                messagebox.showinfo(title="Password Updated", message=f"Password for {account} has been updated.")
        update_button = Button(update_window, text="Update Password", command=update_password, bg="#00bfff", fg="white")
        update_button.pack(pady=10)
    else:
        messagebox.showwarning(title="No password found", message=f"No password found for {account}")

update_password_button = Button(output_frame, text="Update Password", command=update_password_callback, bg="#00bfff", fg="white")
update_password_button.pack(side=TOP, padx=5, pady=10)

# Creating the button to delete a password
def delete_password_callback():
    account = account_entry.get()
    password = get_password(account)
    if password:
        confirmation = messagebox.askquestion(title="Delete Password", message=f"Are you sure you want to delete the password for {account}?")
        if confirmation == "yes":
            del passwords[account]
            messagebox.showinfo(title="Password Deleted", message=f"Password for {account} has been deleted.")
    else:
        messagebox.showwarning(title="No password found", message=f"No password found for {account}")

delete_password_button = Button(output_frame, text="Delete Password", command=delete_password_callback, bg="#00bfff", fg="white")
delete_password_button.pack(side=TOP, padx=5, pady=10)

# Creating the button to show the passwords
show_passwords_button = Button(output_frame, text="Show Passwords", command=show_passwords, bg="#00bfff", fg="white")
show_passwords_button.pack(side=TOP, padx=5, pady=10)

# exit the program
def exit_program():
    root.destroy()

exit_button = Button(output_frame, text="Exit", command=exit_program, bg="#00bfff", fg="white")
exit_button.pack(side=TOP, padx=5, pady=10)

# Packing the frames
input_frame.pack(fill=X)
output_frame.pack(fill=X)

root.mainloop()