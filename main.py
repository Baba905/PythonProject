from tkinter import *
from tkinter import messagebox
import random
import pyclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    #def genearate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    chosen_letters = [random.choice(letters) for _ in range(nr_letters)]
    chosen_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    chosen_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = chosen_numbers+chosen_letters+chosen_symbols
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyclip.copy(password)
    #print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    web = website_entry.get()
    email = email_entry.get()
    passw = password_entry.get()

    new_data = {
        web: {
            "email": email,
            "password" : passw,
        }
    }

    if len(web)==0 or len(passw)==0:
        messagebox.showwarning(title="Missing Entry", message="Attention, some entries are not filled")
    else:
        line = web+"|"+email+"|"+passw+"\n"
        is_ok = messagebox.askokcancel(title="Verification of information", message=f"Check your information\n Website:{web}\n Email:{email}\n, Password:{passw}")
        if is_ok:
            try:
                #print("Try")
                with open("data.json", "r") as file:
                    # file.write(line)
                    data = json.load(file)
                    #print("file loaded")
                    data.update(new_data)

            except FileNotFoundError:
                with open("data.json", "w") as file:
                    #file.write(line)
                    #print("Exception")
                    json.dump(new_data, file, indent=4)
            else:
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)

            website_entry.delete(0, END)
            password_entry.delete(0, END)


#----------------------------- FIND PASSWORD--------------------------- #
def find_password():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showwarning(title="File Not Found", message="There is no password registred")
    else:
        search_website = website_entry.get()

        try:
            website_data = data[search_website]
        except KeyError:
            messagebox.showwarning(title="Not Website", message="No details for the website exists")
        else:
            search_email = website_data["email"]
            search_password = website_data["password"]

            messagebox.showinfo(title=f"{search_website}", message=f"Email : {search_email}\n Password : {search_password}")
    finally:
        website_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
#window.minsize(width=500, height=500)
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

# Website Label
website = Label(text="Website:")
website.grid(column=0, row=1)

# Email Label
email = Label(text="Email/Username:")
email.grid(column=0, row=2)

# Password Label
password = Label(text="Password:")
password.grid(column=0, row=3)

# Website entry
website_entry = Entry(width=33)
website_entry.grid(column=1, row=1)
website_entry.focus()

# Email entry
email_entry = Entry(width=52)
email_entry.grid(column=1,row=2, columnspan=2)
email_entry.insert(0,"baba@gmail.com")

# Password entry
password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

# Button generate
generate = Button(text="Generate Password")
generate.grid(column=2, row=3)
generate["command"] = generate_password

# Button add
add = Button(text="Add", width=43)
add.grid(column=1, row=4, columnspan=2)
add["command"] = save_password

#Button search
search = Button(text="Search", width=15)
search.grid(column=2, row=1)
search["command"] = find_password
window.mainloop()

