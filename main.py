from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1, sticky="E")

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2, sticky="E")

password_label = Label(text='Password:')
password_label.grid(column=0, row=3, sticky="E")


website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW")

password_button = Button(text='Generate Password')
password_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text='Add', width=36)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()