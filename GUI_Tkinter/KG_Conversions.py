from tkinter import *

window = Tk()       # Declaring starting
window.title("Conversion of Weight")

def conversion():
    grams = float(e1_value.get())*1000
    t1.insert(END, grams)
    pounds = float(e1_value.get())*2.20462
    t2.insert(END, pounds)
    ounces = float(e1_value.get())*35.274
    t3.insert(END, ounces)

# User KiloGram
l = Label(window, text="kg")
l.grid(row=0, column=0)

e1_value=StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

b = Button(window, activebackground="green", text="Execute", command=conversion)        # here don't pass () in km_to_miles, it's not a usual function code
b.grid(row=0, column=2)
b.bell()                       # To ring a bell when the application starts

# Grams
t1 = Text(window, height=1, width=25)
t1.grid(row=1, column=0)

l1 = Label(window, text="grams")
l1.grid(row=1, column=1)

# Pounds
t2 = Text(window, height=1, width=25)
t2.grid(row=2, column=0)

l2 = Label(window, text="pounds")
l2.grid(row=2, column=1)

# Ounces
t3 = Text(window, height=1, width=25)
t3.grid(row=3, column=0)

l3 = Label(window, text="ounces")
l3.grid(row=3, column=1)


window.mainloop()   # Declaring Ending
