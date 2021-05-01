import sqlite3
from tkinter import *
from tkinter import StringVar

main_window = Tk()
main_window.title('FindYourCar')
main_window.geometry('1000x700')
main_window.configure(background='white')
C = Canvas(main_window, bg="white", height=2500, width=2500)
C.pack()
rectangle = C.create_rectangle(0, 0, 1050, 60, fill="yellow")


# database function for seller window
def database(seller=None):
    name1 = username.get()
    pas = password.get()
    em = email.get()
    v = v0.get()
    conn = sqlite3.connect('/home/athanpan/Έγγραφα/FindYourCar/findyourcar.db')
    with conn:
        cursor = conn.cursor()
    cursor.execute('INSERT INTO USERS (user_name,user_password,email,role) VALUES(?,?,?,?)', (name1, pas, em, v))
    conn.commit()

# commands for register button behavior in sign up window
def sign_up_button():
    database()
    register_screen.destroy()
    login()

def sign_up():
    # The Toplevel widget work pretty much like Frame,
    # but it is displayed in a separate, top-level window.
    # Such windows usually have title bars, borders, and other “window decorations”.
    # And in argument we have to pass global screen variable

    global register_screen
    register_screen = Toplevel(main_window)
    register_screen.title("Sign Up Seller")
    register_screen.geometry("1000x700")
    register_screen.configure(background='white')
    # p = Canvas(register_screen, bg="white", height=2500, width=2500).pack()

    # Set text variables
    global username
    global password
    global email
    global v0
    username = StringVar()
    password = StringVar()
    email = StringVar()
    v0 = StringVar()
    v0.set(1)

    # Set label for user's instruction
    Label(register_screen, text="Please enter details below.", bg="yellow", font=("calibri", 20)).pack()
    Label(register_screen, text="", font=("calibri", 20), bg="white").pack()

    # Set username label
    username_lable = Label(register_screen, text="Username * ", font=("calibri", 20), bg="yellow").pack()

    # Set username entry
    # The Entry widget is a standard Tkinter widget used to enter or display a single line of text.

    username_entry = Entry(register_screen, textvariable=username).pack(pady=15)

    # Set password label
    password_lable = Label(register_screen, text="Password * ", font=("calibri", 20), bg="yellow").pack()

    # Set password entry
    password_entry = Entry(register_screen, textvariable=password, show='*').pack(pady=15)

    # Set email label
    email_lable = Label(register_screen, text="Email * ", font=("calibri", 20), bg="yellow").pack()

    # Set password entry
    email_entry = Entry(register_screen, textvariable=email).pack(pady=15)


    Label(register_screen, text="", font=("calibri", 20), bg="white").pack()

    # Set role label
    role_lable = Label(register_screen, text="Role * ", font=("calibri", 20), bg="yellow")
    role_lable.place(x=455, y=335)
    r1 = Radiobutton(register_screen, text="seller", bg="yellow", variable=v0, value='seller')
    r2 = Radiobutton(register_screen, text="client", bg="yellow", variable=v0, value='client')
    r1.place(x=465, y=380)
    r2.place(x=465, y=410)

    # Set register button
    b = Button(register_screen, text="Sign Up",font=("calibri", 20), width=20, height=1, bg="yellow", relief="solid", command=sign_up_button).pack(pady=90)



def seller_menu():
    x = 0


def client_menu():
    y = 0;


# define login function
def login():
    login_screen = Toplevel(main_window)
    login_screen.title("Login")
    login_screen.geometry("1000x700")
    login_screen.configure(background='white')
    Label(login_screen, text="Please enter details below to login.", font=("calibri", 20), bg="yellow").pack()
    Label(login_screen, text="", font=("calibri", 20), bg="white").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    Label(login_screen, text="Username * ", font=("calibri", 20), bg="yellow").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="", font=("calibri", 20), bg="white").pack()

    Label(login_screen, text="Password * ", font=("calibri", 20), bg="yellow").pack(pady=3)
    password__login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password__login_entry.pack()
    Label(login_screen, text="", font=("calibri", 20), bg="white").pack()

    Button(login_screen, text="Login", font=("calibri", 20), width=20, height=1, bg="yellow", relief="solid").pack()



# Buttons
button1 = Button(text='Sign up', bg='yellow', font="bold", width=15, relief="solid", pady=8, command=sign_up)
button1.place(x=700, y=10)

button2 = Button(text='Login', bg='yellow', font="bold", width=15, relief="solid", pady=8, command=login)
button2.place(x=850, y=10)

photo = PhotoImage(file="/home/athanpan/Έγγραφα/FindYourCar/FindYourCar.png")
varun_label = Label(image=photo)
varun_label.place(x=380, y=200)

main_window.mainloop()
