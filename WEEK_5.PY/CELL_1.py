import tkinter as tk
from tkinter import messagebox


#handling button click event
def button_click():
 print("Button Clicked!")

#show an information message box
messagebox.showinfo("Info", "Welcome to cos 102 GUI APP! \n")

#Ask for confirmation
result = messagebox.askyesno("confirmation","Do you want to continue ")
# create the main window
root = tk.Tk()
root.title("Home page")
root.geometry("300x100")
#Add a label widget
label = tk.Label(root, text="Hello Friend \n")
label.pack()
#Add a button widget
button = tk.Button (root,text="Click Me!", command=button_click)
button.pack()
#styling the button widget
button.config(fg="red",bg="yellow")
#start the event loop
root.mainloop()

