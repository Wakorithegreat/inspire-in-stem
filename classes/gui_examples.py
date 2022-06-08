#!/usr/bin/python
###########################
#gui examples using ktinker
#name :john wakori
# date : 23/5/20
##########################

from tkinter import *

window = Tk()
window.title("welcome to my website")
window.configure(bg='magenta')
window.geometry("700x600")# fixiing background
name = Label(window,text = "VIBIN",font =("arial ",100))

f_name = Label(window,text= "first name : ",font=("arial ",50))
s_name = Label(window,text= "second name : ",font=("arial ",50))
name.grid(column = 50 , row = 100)
f_name.grid(column = 60 , row = 100)
s_name.grid(column = 60 , row =120 )

Btn = Button(window,text = "sign up ",bg="blue",fg="purple")
Btn.grid(column = 100, row = 180)
f_name_box = Entry(window,width=50)
f_name_box.grid(column = 100 ,row=100)
s_name_box = Entry(window,width=50)
s_name_box.grid(column = 100 ,row=120)
def open_popup():
    top = Toplevel(window)
    top.title("pop up window")
    top.configure(bg = 'blue')
    msg = Label(top,text= "welcome to the pop up",font=("mistral 18"),command = open_popup().pack())
txt_box = Entry(window,width = 30)
txt_box.grid(column = 70,row= 40)
xt_box = Entry(window,width = 30)
txt_box.grid(column = 70,row= 40)

    
window.mainloop()