from tkinter import *
import secrets
from tkinter import messagebox
import pyperclip
import subprocess 
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generateit():
    password1 = secrets.token_urlsafe(8)
    passen.insert(0, password1)
    pyperclip.copy(password1)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #




def saveit():
    web = entryyweb.get()
    password = passen.get()
    email =  emailen.get()
    is_ok = messagebox.askokcancel(title="Info", message="You Fuckin Sure ?")

    struc = {
        web: {
            "password": password,
            "email": email
        }
    }
    
    if is_ok:
        try:

            with open("data.json", 'r') as s:
                data = json.load(s)
                print(data)
                
        except FileNotFoundError:
            with open("data.json", 'w') as s:
                json.dump(struc, s, indent=4)
        
        else:
            data.update(struc)
            with open("data.json", "w") as s:
                json.dump(data, s, indent=4)
            


        finally:
            entryyweb.delete(0, END)
            emailen.delete(0, END)
            passen.delete(0, END)

            
        


def seatchit():
    tex =  entryyweb.get()
    with open("data.json", 'r') as data:
        te = json.load(data)
        ket = list(te.keys())
        print(ket)

        for item in ket:
            if item == tex:
                infoo = f"Email: {te[item]['email']}\n"  + f"Password: {te[item]['password']}"
                messagebox.showinfo(title=tex, message=infoo)
                entryyweb.delete(0, END)
            else:
                messagebox.showerror(title="not found" , message="didn't find it" )
                entryyweb.delete(0, END)

    
    
    

    

        




# ---------------------------- UI SETUP ------------------------------- #




win  = Tk()
win.title("Password manager")

win.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)

imgy = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=imgy)
canvas.grid(column=1, row=0)

texyweb = Label(text="website")
texyweb.grid(column=0, row=1)

emailla  = Label(text="Email/Username")
emailla.grid(column=0, row=2)

textpass = Label(text="Password")
textpass.grid(row=3, column=0)


entryyweb = Entry(width=35)
entryyweb.grid(column=1, row=1)
entryyweb.focus()


emailen = Entry(width=35)
emailen.grid(row=2, column=1)

passen = Entry(width=20, text="ads")
passen.grid(row=3, column=1)

passbun = Button(text="Generate Password", command=generateit)
passbun.grid(row=3, column=2, columnspan=2)

search = Button(text="Search", command=seatchit)
search.grid(column=3, row=1)

addbun = Button(text="ADD", command=saveit)
addbun.grid(column=1, row=4, columnspan=2)


win.mainloop()