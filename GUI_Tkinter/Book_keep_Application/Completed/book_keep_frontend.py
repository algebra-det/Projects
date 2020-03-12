from tkinter import *
import Book_keep_backend            # our created module for backend work i.e. Sqlite3


def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]         # just to take the first value of the tuple
        selected_tuple = list1.get(index)       # it returns the tuple at any index
        # now we will also fill the entries with the details of the selected tuple()
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass

def view_command():
    list1.delete(0,END)                     # here 0 is uesd to clear from index 0 to end
    for row in Book_keep_backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in Book_keep_backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)

def insert_command():
    Book_keep_backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def delete_command():
    Book_keep_backend.delete(selected_tuple[0])
    view_command()

def update_command():
    Book_keep_backend.update(selected_tuple[0],title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    print(selected_tuple[0],title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    # We can't pass the selected_tuple[1],[2].. because these are not defined to be in string or INTEGER
    # that's why we first, select the entity from the Listbox and than print them in the values in their respective fields
    # and then thake the values from the field and pass it to the update function

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

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

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

list1.bind("<<ListboxSelect>>",get_selected_row)

# Creating Buttons for View all, Search Entry, Add Entry, Update, Delete, Close
b1 = Button(window, text="View All", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search Entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add Entry", width=12, command=insert_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)     # command to destroy and close the window
b6.grid(row=7, column=3)


# Creating Checkbutton
Checkbutton(window, text="Preserve Aspects").grid(row=8, column=0)


window.mainloop()


""" If you want to convert this into an .exe file than use 'pyinstaller', installing it by using command 'pip install pyinstaller'
    goto the working directory where your files are both fronend and backend and (any other file important for the app)
    than use :
    pyinstaller Book_keep_frontend.py
    the above command will also make many other files in the directory for troubleshooting purpose
    if you don't want to have such files than use 'pyinstaller -- onefile Book_keep_frontend.py'
    although after the .exe file is created , and when when you double-click to open it
    it will also open a CMD in the background , so in order to exclude that use "--windowed"
    so the final syntax will be:

        pyinstaller --onefile --windowed Book_keep_frontend.py

"""
