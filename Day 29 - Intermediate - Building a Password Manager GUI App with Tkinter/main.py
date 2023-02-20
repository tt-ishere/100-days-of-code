from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    letter_list =[random.choice(letters) for char in range(nr_letters)]
    numbers_list = [random.choice(letters) for num in range(nr_numbers)]
    symbol_list = [random.choice(letters) for sym in range(nr_symbols)]
    password_list = letter_list + numbers_list + symbol_list
    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            'email': email,
            'password': password
        }
    }
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Empty Field", message="Please don't leave any field empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data 
                data = json.load(data_file)
        except FileNotFoundError:
            # saving updated data
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:   
            # updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)     
            
            
# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    website = web_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"Data file not found")  
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title=website, message=f"No details for {website} exists")
    
    
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200,highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
web_label = Label(text="Website")
web_label.grid(row=1, column=0)

email_label = Label(text="Email")
email_label.grid(row=2, column=0)
 
password_label = Label(text="Password")
password_label.grid(row=3, column=0)

# Entries 
web_entry = Entry(width=40)
web_entry.grid(row=1, column=1)
web_entry.focus( )

email_entry = Entry(width=59)
email_entry.grid(row=2, column=1,columnspan=2)
email_entry.insert(0, "enoch260@gmail.com")

password_entry = Entry(width=40)
password_entry.grid(row=3, column=1)

# Buttons
pass_button = Button(text="Generate Password",width=14, command=gen_password)
pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=50, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search",width=14, command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()