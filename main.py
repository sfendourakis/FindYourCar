import sqlite3
from tkinter import *
from tkinter import StringVar
from tkinter import messagebox as ms
from tkinter import filedialog
import seller

import seller

global main_window
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

# database function for car upload
def database_car(seller=None):
    mod = model.get()
    ye = year.get()
    fuel = engine_fuel_type.get()
    hp = engine_hp.get()
    cylinders = engine_cylinders.get()
    transmission = transmission_type.get()
    wheels = driven_wheels.get()
    doors = number_of_doors.get()
    market = market_category.get()
    size = vehicle_size.get()
    style = vehicle_style.get()
    conn = sqlite3.connect('/home/athanpan/Έγγραφα/FindYourCar/findyourcar.db')
    with conn:
        cursor = conn.cursor()
    cursor.execute('INSERT INTO CARS (model,year,engine_fuel_type,engine_hp,engine_cylinders,transmission_type,driven_wheels,number_of_doors,market_category,vehicle_size,vehicle_style) VALUES(?,?,?,?,?,?,?,?,?,?,?)', (mod,ye,fuel,hp,cylinders,transmission,wheels,doors,market,size,style))
    conn.commit()

def submit_car_button():
        database_car()
        upload_cars.destroy()
        # seller_menu()

def login_to_seller_or_admin():
    us_verify = username_verify.get()
    pass_verify = password_verify.get()
    conn = sqlite3.connect('/home/athanpan/Έγγραφα/FindYourCar/findyourcar.db')
    with conn:
        cursor = conn.cursor()
    cursor.execute("SELECT * FROM USERS WHERE user_name=? AND user_password=?", (us_verify, pass_verify))
    records = cursor.fetchall()
    for row in records:
        r = row[4]

    if records:  # An empty result evaluates to False.
        if r == 'seller':
            seller.seller_menu()
        else:
            client_menu()
    else:
        ms.showerror('Oops!', 'Username Not Found.')


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
    b = Button(register_screen, text="Sign Up", font=("calibri", 20), width=20, height=1, bg="yellow", relief="solid",
               command=sign_up_button).pack(pady=90)


def database_info():
    info_info = info.get()
    conn = sqlite3.connect('/home/athanpan/Έγγραφα/FindYourCar/findyourcar.db')
    with conn:
        cursor = conn.cursor()
    cursor.execute('INSERT INTO INFO (info) VALUES(?)', (info_info,))
    conn.commit()


def submit_info_button():
    database_info()
    upload_info_screen.destroy()
    # seller_menu()


def upload_info():
    global upload_info_screen
    global info
    info = StringVar()
    upload_info_screen = Toplevel(main_window)
    upload_info_screen.title("Upload info menu")
    upload_info_screen.geometry("1000x700")
    upload_info_screen.configure(background='white')
    Label(upload_info_screen, text="Welcome to upload info menu.", bg="yellow", font=("calibri", 20)).pack()
    Label(upload_info_screen, text="Please enter your info below.", bg="yellow", font=("calibri", 20)).pack(pady=15)
    info_entry = Entry(upload_info_screen, textvariable=info).pack(pady=50)
    # Set submit info button
    Button(upload_info_screen, text="Submit info", font=("calibri", 20), width=20, height=1, bg="yellow",
           relief="solid",
           command=submit_info_button).pack(pady=90)

"""
def seller_menu():
    global seller_menu
    seller_menu = Toplevel(main_window)
    seller_menu.title("Seller menu")
    seller_menu.geometry("1000x700")
    seller_menu.configure(background='white')
    Label(seller_menu, text="Welcome to seller menu.", bg="yellow", font=("calibri", 20)).pack()

    Label(seller_menu, text="To upload information for you:", bg="yellow", font=("calibri", 20)).pack(pady=85)
    Button(seller_menu, text="Upload Info", font=("calibri", 20), width=20, height=1, bg="yellow", relief="solid",
           command=upload_info).pack(pady=5)
    Label(seller_menu, text="To upload your cars:", bg="yellow", font=("calibri", 20)).pack(pady=85)
    Button(seller_menu, text="Upload Car", font=("calibri", 20), width=20, height=1, bg="yellow", relief="solid",
           command=upload_cars).pack(pady=5)
"""

def upload_cars():
    global upload_car_screen
    global model
    global year
    global engine_fuel_type
    global engine_hp
    global engine_cylinders
    global transmission_type
    global driven_wheels
    global number_of_doors
    global market_category
    global vehicle_size
    global vehicle_style
    global images
    model = StringVar()
    year = StringVar()
    engine_fuel_type = StringVar()
    engine_hp = StringVar()
    engine_cylinders = StringVar()
    transmission_type = StringVar()
    driven_wheels = StringVar()
    number_of_doors = StringVar()
    market_category = StringVar()
    vehicle_size = StringVar()
    vehicle_style = StringVar()
    upload_car_screen = Toplevel(main_window)
    upload_car_screen.title("Upload info menu")
    upload_car_screen.geometry("1000x700")
    upload_car_screen.configure(background='white')
    Label(upload_car_screen, text="Welcome to upload car menu.", bg="yellow", font=("calibri", 20)).pack()
    Label(upload_car_screen, text="Please enter the car feature below.", bg="yellow", font=("calibri", 20)).pack()
    Label(upload_car_screen, text="Model.", bg="yellow", font=("calibri", 15)).pack()
    Entry(upload_car_screen, textvariable=model).pack()
    Label(upload_car_screen, text="Year.", bg="yellow", font=("calibri", 15)).pack()
    Entry(upload_car_screen, textvariable=year).pack()
    Label(upload_car_screen, text="Engine fuel type.", bg="yellow", font=("calibri", 15)).pack()
    Entry(upload_car_screen, textvariable=engine_fuel_type).pack()
    Label(upload_car_screen, text="Engine hp.", bg="yellow", font=("calibri", 15)).pack()
    Entry(upload_car_screen, textvariable=engine_hp).pack()
    Label(upload_car_screen, text="Engine cylinders.", bg="yellow", font=("calibri", 15)).pack()
    Entry(upload_car_screen, textvariable=engine_cylinders).pack()
    Label(upload_car_screen, text="Transmission type.", bg="yellow", font=("calibri", 15)).pack()
    Entry(upload_car_screen, textvariable=transmission_type).pack()
    Label(upload_car_screen, text="Driven wheels.", bg="yellow", font=("calibri", 15)).pack()
    Entry(upload_car_screen, textvariable=driven_wheels).pack()
    Label(upload_car_screen, text="Number of doors.", bg="yellow", font=("calibri", 15)).pack()
    Entry(upload_car_screen, textvariable=number_of_doors).pack()
    Label(upload_car_screen, text="Market category.", bg="yellow", font=("calibri", 15)).pack()
    Entry(upload_car_screen, textvariable=market_category).pack()
    Label(upload_car_screen, text="Vehicle size.", bg="yellow", font=("calibri", 15)).pack()
    Entry(upload_car_screen, textvariable=vehicle_size).pack()
    Label(upload_car_screen, text="Vehicle style.", bg="yellow", font=("calibri", 15)).pack()
    Entry(upload_car_screen, textvariable=vehicle_style).pack()
    # Set submit button
    Button(upload_car_screen, text="Submit car", font=("calibri", 20), width=20, height=1, bg="yellow", relief="solid",
           command=submit_info_button).pack()
    upload_car_screen.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                            filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png"),
                                                                       ("all files", "*.*")))
    print(upload_car_screen.filename)


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

    Button(login_screen, text="Login", font=("calibri", 20), width=20, height=1, bg="yellow", relief="solid",
           command=login_to_seller_or_admin).pack()


# Buttons
button1 = Button(text='Sign up', bg='yellow', font="bold", width=15, relief="solid", pady=8, command=sign_up)
button1.place(x=700, y=10)

button2 = Button(text='Login', bg='yellow', font="bold", width=15, relief="solid", pady=8, command=login)
button2.place(x=850, y=10)

photo = PhotoImage(file="/home/athanpan/Έγγραφα/FindYourCar/FindYourCar.png")
varun_label = Label(image=photo)
varun_label.place(x=380, y=200)

main_window.mainloop()
