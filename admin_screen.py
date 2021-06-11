
from tkinter import *

admin_screen = Tk()
admin_screen.title('Admin Screen')
admin_screen.geometry('1000x700')
admin_screen.configure(background='white')
C = Canvas(admin_screen, bg="white", height=2500, width=2500)
C.pack()
rectangle = C.create_rectangle(0, 0, 1050, 60, fill="yellow")




Y=Button(admin_screen, text="Reports", width=6)
Y_window = C.create_window(10, 200, anchor=W, window=Y)
X = Button(admin_screen, text="New Car", width=6)
X_window = C.create_window(10, 400, anchor=W, window=X)


admin_screen.mainloop()


