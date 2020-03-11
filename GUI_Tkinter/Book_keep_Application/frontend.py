from tkinter import *

window = Tk()
window.title("Book Keep")

# All LABELING i.e. Title, Year, Author, ISBN
l1 = Label(window, text="Title")              # sticky means aligninig the text in any one
l1.grid(row=0, column=0, sticky=W)            # direction i.e. N,E,S,W

#OR
l2 = Label(window, text="Year").grid(row=1, column=0, sticky=W)

l3 = Label(window, text="Author")
l3.grid(row=0, column=2, sticky=W)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2, sticky=W)


# All values taking variables for Title, Year, Author and ISBN
title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

year_text = StringVar()
e2 = Entry(window, textvariable=year_text)
e2.grid(row=1, column=1)

author_text = StringVar()
e3 = Entry(window, textvariable=author_text)
e3.grid(row=0, column=3)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)


# Crating a ListBox
list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

# Creating Scrollbar
sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

#configuring Scrollbar to the Listbox
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)


# Creating Buttons for View all, Search Entry, Add Entry, Update, Delete, Close
b1 = Button(window, text="View All", width=12)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search Entry", width=12)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add Entry", width=12)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update", width=12)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete", width=12)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12)
b6.grid(row=7, column=3)


# Creating Checkbutton
Checkbutton(window, text="Preserve Aspects").grid(row=8, column=0)



window.mainloop()
