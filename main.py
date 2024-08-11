#Imports tkinter and englisttohindi.englisttohindi import EngtoHindi

# import modules
from tkinter import *
from englisttohindi.englisttohindi import EngtoHindi




def eng_to_hindi():
    trans = EngtoHindi(str(e.get()))
    res = trans.convert
    result.set(res)  
 
# object of tkinter
# and background set for grey
master = Tk()
master.configure(bg = 'light grey')
master.title('Translator')

 
# Variable Classes in tkinter
result = StringVar()
head=Label(master,text='English To Hindi Translator')
head.place(x=300,y=0)
# Creating label for each information
# name using widget Label

Label(master, text="Enter Text : " , bg = "light grey").grid(row = 5, sticky = W)
Label(master, text="Result :", bg = "light grey").grid(row = 7, sticky = W)
 
# Creating label for class variable
# name using widget Entry
Label(master, text="", textvariable=result,bg = "light grey").grid(row = 9,sticky = W)
 
e = Entry(master, width = 100)
e.grid(row = 5, column = 1)
 
# creating a button using the widget 
# Button that will call the submit function
b = Button(master, text = "Show", command = eng_to_hindi, bg = "red")
b.grid(row = 1, column = 2, columnspan = 2, rowspan = 2, padx = 5, pady = 5,)
 
mainloop()