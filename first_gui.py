import tkinter as tk
def hi():
	
 respond_label.config(text="Hello there")	      
root=tk.Tk()
root.title("Strings")    
label=tk.Label(root ,text="Salutation" )    
label.pack()
button=tk.Button(root,text="Push the button", command=hi)
button.pack()
respond_label=tk.Label(root,text="")
respond_label.pack()
root.geometry("600x300")
root.mainloop()






