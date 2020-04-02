import tkinter
from tkinter import filedialog as fd
from tkinter import Menu

root = tkinter.Tk(className="Editor")  #forms a window through the tkinter module
text=tkinter.Text(root) #this line is for being able to add text in the window
text.grid() #grid method 
def saveas(): #basic function for saving file
    global text  
    txt = text.get("1.0", "end-1c") #return text index to index
    save_location=fd.asksaveasfilename()
    doc=open(save_location, "w+") #write file in a location
    doc.write(txt)
    doc.close()
button=fd.Button(root, text="Save", command=saveas) 
button.grid()
root.mainloop()

