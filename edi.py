import tkinter as tk
from tkinter import filedialog as fd
from tkinter.filedialog import askopenfilename
from tkinter import Menu

window = tk.Tk(className="Editor")  #forms a window through the tkinter module

def saveas(): #basic function for saving file
    global text  
    txt = text.get("1.0", "end-1c") #return text index to index
    file_name=fd.asksaveasfilename()
    doc=open(file_name, "w+") #write file in a location
    doc.write(txt)
    doc.close()


def open_file():
    filename = askopenfilename(initialdir = "/home", title = "Select file")
    f = open(filename)
    text = f.read()      #can't insert the data from the file to the window for now


menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=open_file, background = "black", foreground = "white")
# filemenu.add_separator()
filemenu.add_command(label="Save", command=saveas, background = "black", foreground = "white")
# filemenu.add_separator()
filemenu.add_command(label="Exit", command=window.quit, background = "black", foreground = "white")
menubar.add_cascade(label="File", menu=filemenu, background = "black", foreground = "white")
window.config(menu=menubar)


text=tk.Text(window) #this line is for being able to add text in the window 
text.pack(fill = tk.BOTH, expand = True)


window.mainloop()
