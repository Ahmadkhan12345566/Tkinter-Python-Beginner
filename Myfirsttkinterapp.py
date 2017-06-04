# -*- coding: utf-8 -*-
"""
Created on Tue May 30 12:33:44 2017

@author: Ahmad khan
"""
import tkinter
import mysql.connector
root = tkinter.Tk()
cnx = mysql.connector.connect(user='obe', database='obe',password='obe')
cursor = cnx.cursor()
l2="kk2"
#function
def hello(event):

    add_employee = ("INSERT INTO abc "
               "(name, anting) "
               "VALUES ('1', '1')")
    cursor.execute(add_employee)
    cnx.commit()

    cursor.close() 
    cnx.close()


l1 = tkinter.Label(text=l2, fg="black", bg="white").pack()
t1 = tkinter.Text( fg="black", bg="white",).pack()
b1 = tkinter.Button(text="Test", fg="black", bg="white",width="50")

#buindingbutton
b1.bind('<Button-1>', hello)
b1.pack()

root.title("My First Python App using tkinter")

root.geometry("500x500+400+100")
root.mainloop()   
           
