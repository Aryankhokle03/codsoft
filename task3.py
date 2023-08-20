############################## PASSWORD GENERATOR ############################################
import random
from tkinter import *
from tkinter.ttk import *

# Function for generation of password
def generate():
    username = username_entry.get()
    length = int(length_entry.get())
    password = generate_random_password(length)
    entry.delete(0, END)
    entry.insert(0, password)

# Function to generate a random password
def generate_random_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 !@#$%^&*()"
    password = "".join(random.choice(characters) for word in range(length))
    return password

# Main Function
root = Tk()
root.title("Password Generator")

username_label = Label(root, text="Username")
username_label.grid(row=0, padx=10, pady=10)
username_entry = Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=10)

length_label = Label(root, text="Password Length")
length_label.grid(row=1, padx=10, pady=10)
length_entry = Entry(root)
length_entry.grid(row=1, column=1, padx=15, pady=15)

generate_button = Button(root, text="Generate password", command=generate)
generate_button.grid(row=2, columnspan=2, padx=10, pady=10)

password_label = Label(root, text="Generated Password")
password_label.grid(row=3, padx=10, pady=10)
entry = Entry(root)
entry.grid(row=3, column=1, padx=10, pady=10)

root.mainloop()