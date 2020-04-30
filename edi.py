import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd

window = tk.Tk(className="Editor")  #forms a window through the tkinter module

def saveas(): #basic function for saving file
    global text  
    txt = text.get("1.0", "end-1c") #return text index to index
    file_name = fd.asksaveasfilename()
    doc=open(file_name, "w+") #write file in a location
    doc.write(txt)
    doc.close()


def open_file():
    filename = fd.askopenfilename(initialdir = "/home", title = "Select file")
    f = open(filename)
    text = f.read()      #can't insert the data from the file to the window for now


def about():
    details = """
This is a simple text editor made in python.
    """
    messagebox.showinfo("About", details)


def select_fonts():
	pass

	
menubar = Menu(window)

filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "Open", command = open_file, background = "black", foreground = "white")
filemenu.add_command(label = "Save", command = saveas, background = "black", foreground = "white")
filemenu.add_command(label = "Exit", command = window.quit, background = "black", foreground = "white")
menubar.add_cascade(label = "File", menu = filemenu, background = "black", foreground = "white")

edit = Menu(menubar, tearoff = 0)
edit.add_command(label = "Fonts", command = select_fonts, background = "black", foreground = "white")
# edit.add_cascade(label = "Fonts",menu = edit, background = "black", foreground = "white")
menubar.add_cascade(label = "Edit", menu = edit, background = "black", foreground = "white")

help_menu = Menu(menubar, tearoff = 0)
help_menu.add_checkbutton(label = "About",command = about, background = "black", foreground = "white" )
menubar.add_cascade(label = "Help", menu = help_menu, background = "black", foreground = "white")

window.config(menu=menubar)

text= Text(window) #this line is for being able to add text in the window 
text.config(font="Ariel")
text.pack(fill = BOTH, expand = True)


window.mainloop()
