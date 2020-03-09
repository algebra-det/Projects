from tkinter import *

window = Tk()       # Declaring starting
window.title("First App")

def km_to_miles():
    miles = float(e1_value.get())*1.6
    t1.insert(END, miles)

b1 = Button(window, activebackground="lightgrey", text="Execute", command=km_to_miles)        # here don't pass () in km_to_miles, it's not a usual function code
b1.grid(row=0, column=0)
b1.bell()                       # To ring a bell when the application starts

e1_value=StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width=20)
t1.grid(row=0, column=2)


window.mainloop()   # Declaring Ending
