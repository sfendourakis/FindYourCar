import sqlite3
from cgitb import text
from distutils import command
from re import search
from tkinter import *
from tkinter import StringVar, Label
from turtle import width
from dotenv import load_dotenv
load_dotenv()
import os

database = os.getenv("DATABASE_DIR")


client_screen = Tk()
client_screen.title('Client Screen')
client_screen.geometry('1000x700')
client_screen.configure(background='white')
C = Canvas(client_screen, bg="white", height=2500, width=2500)
C.pack()
rectangle = C.create_rectangle(0, 0, 2500, 60, fill="yellow")

def get_Search():

    conn = sqlite3.connect(database)
    with conn:
        cursor = conn.cursor()

    global Car_Search
    Car_Search=enter_box.get()
    cursor.execute("""SELECT * FROM CARS WHERE Model LIKE '%?%'""", (Car_Search))


global Search_Screen


label1: Label = Label(
                      client_screen,
                      text="Search Car",
                      bg=("yellow"),
                      font=("calibri", 20, "bold"))
label1.place(x=450, y=110)

enter_box = Entry(width=30)
enter_box.place(x=420, y=154)

btn = Button(client_screen,
             text="Search",
             command=get_Search(),
             bg="yellow",
             fg="white",
             font=("calibri", 10, "bold"))
btn.place(x=325, y=150)


photo = PhotoImage(file="/home/rigers/Desktop/Findyourcar/findyourcar.png")
varun_label = Label(image=photo)
varun_label.place(x=380, y=200)
client_screen.mainloop()