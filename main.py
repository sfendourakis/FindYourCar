from tkinter import *
from tkinter import StringVar
import sqlite3

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
    conn = sqlite3.connect('/home/athanpan/Έγγραφα/FindYourCar/findyourcar.db')
    with conn:
        cursor = conn.cursor()
    cursor.execute('INSERT INTO USERS (user_name,user_password,email) VALUES(?,?,?)', (name1, pas, em, ))
    cursor.execute("INSERT INTO ROLES (role_name) VALUES('seller')")
    conn.commit()

# commands for seller's button behavior in sign up window
def sign_up_button1():
    sign_up_seller()
    register_screen1.destroy()

# commands for client's button behavior in sign up window
def sign_up_button2():
    sign_up_client()
    register_screen1.destroy()

def sign_up():
    # The Toplevel widget work pretty much like Frame,
    # but it is displayed in a separate, top-level window.
    # Such windows usually have title bars, borders, and other “window decorations”.
    # And in argument we have to pass global screen variable

    global register_screen1
    register_screen1 = Toplevel(main_window)
    register_screen1.title("Sign Up")
    register_screen1.geometry("1000x700")
    register_screen1.configure(background='white')

    # Set text variables
    username = StringVar()
    password = StringVar()
    email = StringVar()

    # Set label for user's instruction
    Label(register_screen1, text="Please select how to sign up.", bg="yellow", font=("calibri", 20)).pack()
    Label(register_screen1, text="", font=("calibri", 20), bg="white").pack()


    # Set register button
    Button(register_screen1, text="Seller.",font=("calibri", 20), width=20, bg="yellow", relief="solid", command=sign_up_button1).pack(pady=15)
    Button(register_screen1, text="Client.", font=("calibri", 20), width=20, bg="yellow", relief="solid", command=sign_up_button2).pack()

def seller_button():
    database()
    register_screen.destroy()
    login()

def sign_up_seller():
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
    username = StringVar()
    password = StringVar()
    email = StringVar()

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

    # Set register button
    Button(register_screen, text="Sign Up",font=("calibri", 20), width=20, height=1, bg="yellow", relief="solid", command=seller_button).pack()

# database function for client window
def database2():
    name2 = username2.get()
    pas2 = password2.get()
    em2 = email2.get()
    conn = sqlite3.connect('/home/athanpan/Έγγραφα/FindYourCar/findyourcar.db')
    with conn:
        cursor = conn.cursor()
    cursor.execute('INSERT INTO USERS (user_name,user_password,email) VALUES(?,?,?)', (name2, pas2, em2, ))
    cursor.execute("INSERT INTO ROLES (role_name) VALUES('client')")
    conn.commit()

def client_button():
    database2()
    register_screen2.destroy()
    login()

def sign_up_client():
    # The Toplevel widget work pretty much like Frame,
    # but it is displayed in a separate, top-level window.
    # Such windows usually have title bars, borders, and other “window decorations”.
    # And in argument we have to pass global screen variable

    global register_screen2
    register_screen2 = Toplevel(main_window)
    register_screen2.title("Sign Up Client.")
    register_screen2.geometry("1000x700")
    register_screen2.configure(background='white')
    # p = Canvas(register_screen, bg="white", height=2500, width=2500).pack()

    # Set text variables
    global username2
    global password2
    global email2
    username2 = StringVar()
    password2 = StringVar()
    email2 = StringVar()

    # Set label for user's instruction
    Label(register_screen2, text="Please enter details below.", bg="yellow", font=("calibri", 20)).pack()
    Label(register_screen2, text="", font=("calibri", 20), bg="white").pack()

    # Set username label
    username_lable = Label(register_screen2, text="Username * ", font=("calibri", 20), bg="yellow").pack()

    # Set username entry
    # The Entry widget is a standard Tkinter widget used to enter or display a single line of text.

    username_entry = Entry(register_screen2, textvariable=username2).pack(pady=15)

    # Set password label
    password_lable = Label(register_screen2, text="Password * ", font=("calibri", 20), bg="yellow").pack()

    # Set password entry
    password_entry = Entry(register_screen2, textvariable=password2, show='*').pack(pady=15)

    # Set email label
    email_lable = Label(register_screen2, text="Email * ", font=("calibri", 20), bg="yellow").pack()


    # Set password entry
    email_entry = Entry(register_screen2, textvariable=email2).pack(pady=15)


    Label(register_screen2, text="", font=("calibri", 20), bg="white").pack()

    # Set register button
    Button(register_screen2, text="Sign Up",font=("calibri", 20), width=20, height=1, bg="yellow", relief="solid", command=client_button).pack()

def seller_menu():
    x = 0

def client_menu():
    y =0;

# database function for verify user in login form
def database_login():
    name3 = username_verify.get()
    conn = sqlite3.connect('/home/athanpan/Έγγραφα/FindYourCar/findyourcar.db')
    with conn:
        cursor = conn.cursor()
    cursor.execute('SELECT role_name FROM ROLES INNER JOIN USERS ON user_name = ?', (name3))
    conn.commit()
    if cursor == "seller" :
    seller_menu()
    elif cursor == "client" :
    client_menu()
    else :
        print("There isn't this username. Please sign up !!")



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
button1 = Button( text='Sign up', bg='yellow', font="bold" , width=15, relief="solid", pady=8, command=sign_up)
button1.place(x=700, y=10)

button2 = Button( text='Login', bg='yellow', font="bold" , width=15, relief="solid", pady=8, command=login)
button2.place(x=850, y=10)

photo = PhotoImage(file="/home/athanpan/Έγγραφα/FindYourCar/FindYourCar.png")
varun_label = Label(image=photo)
varun_label.place(x=380, y=200)

main_window.mainloop()