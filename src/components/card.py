from tkinter import Canvas
from tkinter import Label

class Card(Canvas):

    def __init__(self, master, contact, **kwargs):
        super().__init__(master, **kwargs)

        self.contact = contact

        self.configure(bg="#BCD6F5", 
                    width=250, 
                    height=100, 
                    cursor="hand2",
                    bd=0,
                    highlightthickness=0)

        name = Label(self, text=self.contact[1], fg="#18445C" ,font=("Arial",12), bg="#BCD6F5")
        name.place(x=12, y=4)
        last_name = Label(self, text= self.contact[2], fg="#18445C", font=("Arial", 12), bg="#BCD6F5")
        last_name.place(x=12, y = 24)
        email = Label(self, text=self.contact[3],fg="#18445C" , font=("Arial",12), bg="#BCD6F5")
        email.place(x= 12, y= 71)
        phone = Label(self, text=self.contact[4], fg="#18445C" ,font=("Arial", 12), bg="#BCD6F5")
        phone.place(x=230, y=4)
