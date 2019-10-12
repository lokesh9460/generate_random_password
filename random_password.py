# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 18:15:28 2019

@author: Lokesh Kumar
"""

import random
from tkinter import *
import string

def generate_password():
    password=[]
    for i in range(5):
        alpha=random.choice(string.ascii_letters)
        symbol=random.choice(string.punctuation)
        numbers=random.choice(string.digits)
        password.append(alpha)
        password.append(symbol)
        password.append(numbers)
		
    y="".join(str(x)for x in password)
    lbl.config(text=y)






root=Tk()
root.geometry("250x200")
btn=Button(root,text="generate password",command=generate_password)
btn.grid(row=2,column=2)
lbl=Label(root,font=("times",15,"bold"))
lbl.grid(row=4,column=2)
root.mainloop()